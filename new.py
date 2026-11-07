import json


FILE_NAME = "planner.json"


# ==================== ЗАВАНТАЖЕННЯ ====================

def load_events():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Помилка! Файл пошкоджений.")
        return {}


# ==================== ЗБЕРЕЖЕННЯ ====================

def save_events(events):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(events, file, ensure_ascii=False, indent=4)

    except Exception:
        print("Помилка при збереженні файлу.")


# ==================== ДОДАВАННЯ ====================

def add_event(events):
    title = input("Назва події: ")
    date = input("Дата (YYYY-MM-DD): ")
    time = input("Час (HH:MM): ")
    description = input("Опис події: ")

    new_id = 1

    if len(events) > 0:
        new_id = max(map(int, events.keys())) + 1

    events[str(new_id)] = {
        "title": title,
        "date": date,
        "time": time,
        "description": description
    }

    save_events(events)

    print("Подію успішно додано!")


# ==================== ПЕРЕГЛЯД ====================

def show_events(events):
    if len(events) == 0:
        print("Подій немає")
        return

    for event_id, event in events.items():
        print()
        print("ID:", event_id)
        print("Назва:", event["title"])
        print("Дата:", event["date"])
        print("Час:", event["time"])
        print("Опис:", event["description"])


# ==================== ВИДАЛЕННЯ ====================

def delete_event(events):
    try:
        event_id = int(input("Введіть ID події: "))

        if str(event_id) in events:
            del events[str(event_id)]

            save_events(events)

            print("Подію видалено!")

        else:
            print("Подію не знайдено")

    except ValueError:
        print("Помилка! ID повинен бути числом.")


# ==================== ПОШУК ЗА ДАТОЮ ====================

def find_by_date(events):
    date = input("Введіть дату (YYYY-MM-DD): ")

    found = False

    for event in events.values():
        if event["date"] == date:
            print(
                event["time"],
                "—",
                event["title"],
                "(" + event["description"] + ")"
            )

            found = True

    if found == False:
        print("Подій на цю дату немає")


# ==================== ГОЛОВНА ПРОГРАМА ====================

events = load_events()


while True:
    print()
    print("--- Персональний планувальник ---")
    print()
    print("1. Додати подію")
    print("2. Переглянути всі події")
    print("3. Видалити подію")
    print("4. Знайти події за датою")
    print("5. Вийти")

    choice = input("Виберіть пункт: ")

    if choice == "1":
        add_event(events)

    elif choice == "2":
        show_events(events)

    elif choice == "3":
        delete_event(events)

    elif choice == "4":
        find_by_date(events)

    elif choice == "5":
        print("Програму завершено.")
        break

    else:
        print("Помилка! Виберіть пункт від 1 до 5.")