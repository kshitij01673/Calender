import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- DB SETUP ----------------
conn = sqlite3.connect("calendar.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    date TEXT,
    time TEXT,
    created_at TEXT
)
""")
conn.commit()


# ---------------- HELPER FUNCTIONS ----------------
def format_time_12hr(time_24):
    t = datetime.strptime(time_24, "%H:%M")
    return t.strftime("%I:%M %p")


def get_events(search=""):
    if search:
        cursor.execute("SELECT * FROM events WHERE title LIKE ?", ('%' + search + '%',))
    else:
        cursor.execute("SELECT * FROM events")
    return cursor.fetchall()


def delete_event(event_id):
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()


# ---------------- UI ----------------
st.set_page_config(page_title="Calendar App", layout="centered")

st.title("📅 My Calendar App")

menu = st.sidebar.selectbox("Menu", ["Add Event", "View Events"])

# ---------------- ADD EVENT ----------------
if menu == "Add Event":
    st.subheader("➕ Add New Event")

    title = st.text_input("Event Title")
    description = st.text_area("Description")

    date = st.date_input("Select Date")
    time = st.time_input("Select Time")

    if st.button("Add Event"):
        if title:
            date_str = date.strftime("%d-%m-%Y")
            time_str = time.strftime("%H:%M")
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                INSERT INTO events (title, description, date, time, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (title, description, date_str, time_str, created_at))

            conn.commit()
            st.success("Event added successfully 🎉")
        else:
            st.warning("Title is required ⚠️")


# ---------------- VIEW EVENTS ----------------
elif menu == "View Events":
    st.subheader("📋 All Events")

    search = st.text_input("🔍 Search by title")

    events = get_events(search)

    if events:
        for event in events:
            event_id, title, desc, date, time, created = event

            st.markdown(f"### 📌 {title}")
            st.write(f"📅 Date: {date}")
            st.write(f"⏰ Time: {format_time_12hr(time)}")
            st.write(f"📝 Description: {desc}")
            st.write(f"🕒 Created: {created}")

            if st.button(f"❌ Delete Event {event_id}"):
                delete_event(event_id)
                st.warning("Event deleted")
                st.rerun()

            st.write("---")
    else:
        st.info("No events found 📭")