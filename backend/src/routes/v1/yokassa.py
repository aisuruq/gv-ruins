from fastapi import APIRouter, HTTPException, Request, status
from src.schemas.yokassa import PaymentRequest
from src.sheets.yokassa import yokassa_sheet
from src.services.yokassa_client import yokassa_client

router = APIRouter()


@router.post("/yokassa-webhook")
def yokassa_info(): ...


@router.post("/create")
def create_order(yokassa: PaymentRequest):
    try:
        response = yokassa_client.create_payment(
            amount=yokassa.amount,
            description=yokassa.description,
        )

        confirmation_url = response.get("confirmation", {}).get("confirmation_url")

        if not confirmation_url:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Не удалось получить ссылку на оплату",
            )

        return {"payment_url": confirmation_url}
    except Exception as e:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Платеж не создан, пожалуйста повторите позднее. ",
        )
