import sqlite3
from datetime import datetime
import os

# ------------------ DB SETUP ------------------
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    time TEXT,
    created_at TEXT
);
""")
conn.commit()


# ------------------ HELPERS ------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_time_12hr(time_24):
    try:
        t = datetime.strptime(time_24, "%H:%M")
        return t.strftime("%I:%M %p").lstrip("0")
    except:
        return "N/A"


def convert_to_24hr(time_str):
    try:
        t = datetime.strptime(time_str, "%I:%M %p")
        return t.strftime("%H:%M")
    except:
        return None


# ------------------ ADD EVENT ------------------
def add_event():
    clear()
    print("=== Add Event ===")

    title = input("Title: ").strip().lower()
    description = input("Description: ").strip()
    date = input("Date (DD-MM-YYYY): ").strip()
    time_input = input("Time (HH:MM AM/PM): ").strip()

    time = convert_to_24hr(time_input)
    if not time:
        print("Invalid time format!")
        input("Press Enter...")
        return

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO events (title, description, date, time, created_at) VALUES (?, ?, ?, ?, ?)",
        (title, description, date, time, created_at)
    )
    conn.commit()

    print("\n✅ Event Added!")
    input("Press Enter...")


# ------------------ VIEW EVENTS ------------------
def view_events():
    clear()
    print("=== View Events ===")

    date = input("Date (DD-MM-YYYY) [Enter to skip]: ").strip()
    title = input("Title [Enter to skip]: ").strip()
    time_input = input("Time (HH:MM AM/PM) [Enter to skip]: ").strip()

    time = convert_to_24hr(time_input) if time_input else None
    if time_input and not time:
        print("Invalid time format!")
        input("Press Enter...")
        return

    query = "SELECT id, title, date, time, description FROM events WHERE 1=1"
    params = []

    if date:
        query += " AND date = ?"
        params.append(date)

    if title:
        query += " AND title LIKE ?"
        params.append(f"%{title.lower()}%")

    if time:
        query += " AND time = ?"
        params.append(time)

    query += " ORDER BY date, time"

    cursor.execute(query, params)
    rows = cursor.fetchall()

    if not rows:
        print("\nNo events found.")
        input("Press Enter...")
        return

    print("\n=== Events ===")
    for row in rows:
        print(f"""
ID          : {row[0]}
Title       : {row[1].title()}
Date        : {row[2]}
Time        : {format_time_12hr(row[3])}
Description : {row[4]}
---------------------------""")

    input("Press Enter...")


# ------------------ SEARCH ------------------
def search_events():
    clear()
    keyword = input("Search keyword: ").strip()

    query = """
    SELECT id, title, date, time, description
    FROM events
    WHERE title LIKE ? OR description LIKE ?
    ORDER BY date, time
    """

    param = f"%{keyword}%"
    cursor.execute(query, (param, param))
    rows = cursor.fetchall()

    if not rows:
        print("No results found.")
        input("Press Enter...")
        return

    print("\n=== Results ===")
    for row in rows:
        print(f"""
ID          : {row[0]}
Title       : {row[1].title()}
Date        : {row[2]}
Time        : {format_time_12hr(row[3])}
Description : {row[4]}
---------------------------""")

    input("Press Enter...")


# ------------------ DELETE ------------------
def delete_event():
    clear()
    print("=== Delete Event ===")

    date = input("Date (DD-MM-YYYY): ").strip()
    title = input("Title: ").strip().lower()

    cursor.execute(
        "SELECT id, time FROM events WHERE date = ? AND title = ?",
        (date, title)
    )
    rows = cursor.fetchall()

    if not rows:
        print("No matching events.")
        input("Press Enter...")
        return

    if len(rows) == 1:
        cursor.execute("DELETE FROM events WHERE id = ?", (rows[0][0],))
        conn.commit()
        print("✅ Event deleted!")
        input("Press Enter...")
        return

    print("\nMultiple events found:")
    for r in rows:
        print(f"ID: {r[0]} | Time: {format_time_12hr(r[1])}")

    time_input = input("Enter time (HH:MM AM/PM): ").strip()
    time = convert_to_24hr(time_input)

    if not time:
        print("Invalid time!")
        input("Press Enter...")
        return

    cursor.execute(
        "DELETE FROM events WHERE date = ? AND title = ? AND time = ?",
        (date, title, time)
    )
    conn.commit()

    print("✅ Event deleted!")
    input("Press Enter...")


# ------------------ MAIN LOOP ------------------
def main():
    while True:
        clear()
        print("""
====== CLI Calendar ======
1. Add Event
2. View Events
3. Search Events
4. Delete Event
5. Exit
""")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            search_events()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")
            input("Press Enter...")


if __name__ == "__main__":
    main()