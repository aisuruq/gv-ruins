from src.models.events import Event
from datetime import datetime
from src.sheets.events import events_sheet


def sync_events_with_db(session):
    events = events_sheet.get_all_events()
    added_events = []

    for event in events:
        try:
            event_dt = parse_event_datetime(event)
        except ValueError as e:
            print(f"Ошибка в дате мероприятия: {e}")
            continue
        
        existing_event = session.query(Event).filter(
            Event.name == event["Название"],
            Event.datetime == event_dt
        ).first()

        if existing_event:
            print(f"Мероприятие '{event['Название']}' на {event_dt} уже существует.")
            continue

        new_event = Event(
            name=event["Название"],
            datetime=event_dt,
            met_place=event["Место встречи"],
            route=event["Маршрут"],
            guid=event["Гид"],
            cost=event["Цена"],
            max_participants=event["Максимальное количество участников"],
            description=event["Описание"],
            details=event["Детали"]
        )

        added_events.append(new_event)

    if added_events:
        try:
            session.add_all(added_events)
            session.commit()
            return {
                "status": "success",
                "message": f"{len(added_events)} мероприятий успешно синхронизированы.",
                "added_events_count": len(added_events)
            }
        except Exception as e:
            session.rollback()
            return {
                "status": "error",
                "message": f"Ошибка при сохранении: {e}"
            }

    return {
        "status": "no_changes",
        "message": "Все мероприятия уже есть в базе."
    }


def parse_event_datetime(event):
    date_str = f"{event['Дата']} {event['Время']}"
    formats = [
        "%d.%m.%Y %H:%M",
        "%Y.%m.%d %H:%M",
        "%d-%m-%Y %H:%M",
        "%d/%m/%Y %H:%M",
        "%Y-%m-%d %H:%M"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Не удалось распарсить дату и время: {date_str}")
