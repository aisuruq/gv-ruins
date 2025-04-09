from pydantic import BaseModel


class PaymentRequest(BaseModel):
    amount: float
    description: str
