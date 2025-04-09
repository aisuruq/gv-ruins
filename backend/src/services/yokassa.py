import uuid
import requests
import base64


class YoKassaClient:
    def __init__(self, shop_id, secret_key):
        self.shop_id = shop_id
        self.secret_key = secret_key
        self.api_url = "https://api.yookassa.ru/v3/"

    def auth_encode(self):
        auth_string = f"{self.shop_id}:{self.secret_key}"
        return base64.b64encode(auth_string.encode()).decode()

    def create_payment(self, amount, description):
        headers = {
            "Content-Type": "application/json",
            "Idempotence-Key": str(uuid.uuid4()),
            "Authorization": f"Basic {self.auth_encode()}",
        }

        data = {
            "amount": {
                "value": str(amount),
                "currency": "RUB",
            },
            "capture": True,
            "confirmation": {
                "type": "redirect",
                "return_url": "http://gvruins.ru",
            },
            "description": description,
        }

        response = requests.post(f"{self.api_url}payments", json=data, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
