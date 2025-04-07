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

    def register(self, name, surname, patronymic, tg_username, event_id):
        if self.is_registered(tg_username, event_id):
            return False

        new_id = self.next_id()
        self.append([new_id, name, surname, patronymic, tg_username, event_id])
        return True

participants_sheet = ParticipantsSheet()