from src.models.events import Event
from datetime import datetime
from src.sheets.events import events_sheet


def sync_events_with_db(session):
    events = events_sheet.get_all_events()
    added_events = []
    
    for event in events:
        print(event)
        try:
            event_dt = datetime.strptime(
                f"{event['Дата']} {event['Время']}", "%d.%m.%Y %H:%M"
            )
        except Exception as e:
            print(
                f"Ошибка при преобразовании даты/времени для мероприятия {event['id']}: {e}"
            )
            continue

        create_event = Event(
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

        new_event = session.add(create_event)
        added_events.append(new_event)

        try:
            session.commit()
        except Exception as e:
            session.rollback()
            return {
                "status": "error",
                "message": "Ошибка при синхронизации с базой данных"
            }
        return {
            "status": "success",
            "message": "Мероприятия успешно синхронизированы с базой данных",
            "added_events_count": len(added_events)
        }
