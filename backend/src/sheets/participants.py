from datetime import datetime
from fastapi import HTTPException, status
from .base import GoogleSheet


class ParticipantsSheet(GoogleSheet):
    def __init__(self):
        super().__init__(sheet_name="gv-ruins", worksheet_name="Участники")

    def is_registered(self, telegram: str, event_id: int):
        participants = self.get_all()
        for row in participants:
            if row["tg_username"] == telegram and int(row["event_id"]) == event_id:
                return True
        return False

    def get_all_participants(self):
        return self.get_all()

    def next_id(self):
        return len(self.get_all()) + 1

    def register(
        self,
        name: str,
        surname: str,
        patronymic: str,
        phone: str,
        tg_username: str,
        event_id: int,
        comment: str,
        payment: int,
        prepayment: int,
    ) -> dict:
        if self.is_registered(tg_username, event_id):
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail="Пользователь уже зарегистрирован на это мероприятия",
            )

        new_id = self.next_id()
        created_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        balance_of_payment = max(payment - prepayment, 0)

        self.append(
            [
                new_id,
                name,
                surname,
                patronymic,
                phone,
                tg_username,
                event_id,
                comment,
                payment,
                prepayment,
                balance_of_payment,
                created_at,
            ]
        )

        return {
            "status": "success",
            "message": "Регистрация прошла успешно. Данные будут обработаны организаторами.",
        }


participants_sheet = ParticipantsSheet()
