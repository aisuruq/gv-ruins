from fastapi import Request
from .base import GoogleSheet


class YokassaSheet(GoogleSheet):
    def __init__(self):
        super().__init__(sheet_name="gv-ruins", worksheet_name="Юкасса")

    def add_order(self, payment_id, amount, description):
        self.append([payment_id, amount, description, "Pending"])


async def yookassa_webhook(request: Request):
    data = await request.json()
    event_type = data.get("event", {}).get("type")

    if event_type == "payment.succeeded":
        payment_data = data["event"]["object"]
        payment_id = payment_data["id"]
        order_amount = payment_data["amount"]["value"]
        order_description = payment_data["description"]

        yokassa_sheet = YokassaSheet()
        yokassa_sheet.add_order(payment_id, order_amount, order_description)

        return {"status": "success"}
    else:
        return {"status": "ignored"}


yokassa_sheet = YokassaSheet()
