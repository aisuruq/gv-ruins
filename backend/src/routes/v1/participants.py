from fastapi import APIRouter
from typing import List
from fastapi import APIRouter, HTTPException, status
from configuration.db_helper import db_helper
from src.repositories.participants_repository import register_participant
from src.schemas.participants import CreateParticipants
from src.sheets.participants import participants_sheet
from src.schemas.yokassa import PaymentRequest
from src.sheets.yokassa import yokassa_sheet
from src.services.yokassa_client import yokassa_client

router = APIRouter()


@router.get("/list", response_model=List[dict])
def get_events():
    return participants_sheet.get_all_participants()


@router.post("/register_and_pay")
def register_and_pay(
    participants: CreateParticipants,
    yokassa: PaymentRequest
):
    try:
        session = db_helper.session_getter()
        register_participant(session, participants)

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

        return {
            "status": "success",
            "message": "Регистрация прошла успешно, перейдите к оплате",
            "payment_url": confirmation_url
        }

    except Exception as e:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Произошла ошибка: {e}"
        )

