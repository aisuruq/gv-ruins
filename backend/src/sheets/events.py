from datetime import datetime
from .base import GoogleSheet


class EventsSheet(GoogleSheet):
    def __init__(self):
        super().__init__(sheet_name="gv-ruins", worksheet_name="Мероприятия")

    def get_event_by_id(self, event_id: int):
        events = self.get_all()
        for event in events:
            if int(event["id"]) == event_id:
                return event
        return None

    def get_all_events(self):
        return self.get_all()

    def get_upcoming_events(self):
        events = self.get_all()
        now = datetime.now()

        def parse_datetime(event):
            try:
                event_dt = datetime.strptime(
                    f"{event['date']} {event['time']}", "%d.%m.%Y %H:%M"
                )
                return event_dt
            except Exception:
                return datetime.max

        sorted_events = sorted(
            [e for e in events if parse_datetime(e) >= now], key=parse_datetime
        )
        return sorted_events


events_sheet = EventsSheet()
