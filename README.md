# 📅 Calendar Event Manager (CLI + GUI)

A simple yet powerful **Python-based calendar application** that lets you manage events efficiently.
This project includes:

* 🖥️ **CLI Version** (Terminal-based)
* 🌐 **GUI Version** using Streamlit

Both versions use **SQLite** for data storage and support adding, viewing, searching, and deleting events.

---

## 🚀 Features

### ✅ Common Features

* Add events with title, description, date, and time
* View events with formatted output
* Search events by keyword
* Delete events easily
* Persistent storage using SQLite database

### 🖥️ CLI Version

* Interactive terminal-based interface
* Filter events by date, title, and time
* Clean and simple navigation

### 🌐 GUI Version (Streamlit)

* User-friendly web interface
* Add and view events visually
* Search functionality
* One-click delete buttons

---

## 🛠️ Tech Stack

* **Python**
* **SQLite3**
* **Streamlit** (for GUI)

---

## 📂 Project Structure

```
.
├── main.py        # CLI-based calendar app
├── withgui.py     # Streamlit GUI app
├── database.db    # CLI database (auto-created)
├── calendar.db    # GUI database (auto-created)
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/calendar-app.git
cd calendar-app
```

### 2. Install dependencies

```
pip install streamlit
```

---

## ▶️ Usage

### 🖥️ Run CLI Version

```
python main.py
```

### 🌐 Run GUI Version

```
streamlit run withgui.py
```

---

## 🧠 How It Works

* Events are stored in an **SQLite database**
* Time is internally stored in **24-hour format** and displayed in **12-hour format**
* CLI version allows advanced filtering
* GUI version provides a smooth interactive experience



---

## 🔮 Future Improvements

* Edit/update events
* Notifications & reminders
* Calendar view (monthly/weekly)
* Export events (CSV/JSON)
* Authentication system

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests. Contributions are welcome!

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Made with ❤️ by *Kshitij*

---

⭐ If you like this project, consider giving it a star!
