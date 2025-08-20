# ⏱️ Advanced Stopwatch App (Python + CustomTkinter)

A modern, feature-rich desktop stopwatch built using Python and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). Designed with real-time precision, lap tracking, and beautiful dark/light themes, this stopwatch is perfect for productivity, workouts, or coding sprints!

---


## 🖥️ Features

* ✅ **Start / Pause / Reset** the stopwatch
* 🧮 **Lap recording** with individual and cumulative times
* 🧹 **Clear laps** with one click
* 🌙 **Dark / Light mode toggle**
* 🕒 Real-time millisecond precision updates
* 🧵 Background threading ensures smooth UI
* 🧩 Clean, responsive UI with scrollable lap list

---

## 🛠 Tech Stack

| Layer | Tool                                                              |
| ----- | ----------------------------------------------------------------- |
| GUI   | [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) |
| Core  | Python Standard Library (`time`, `threading`)                     |
| UX    | Dark/Light Mode, Scrollable Frames                                |
| OS    | Cross-platform (Windows, macOS, Linux)\*                          |

> \*Tested on Windows 11

---

## 💾 Requirements

* Python 3.9 or later
* pip

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
python stopwatch_app.py
```

Make sure you're inside the correct directory before running the above command.

---

## 📦 Clone the Repository

```bash
git clone https://github.com/GITWithAkshay/tkinter-stopwatch-app.git
cd tkinter-stopwatch-app
````

---

## 📁 Project Structure

```bash
tkinter-stopwatch-app/
│
├── stopwatch_app.py         # Main application file
├── README.md                # You're reading it!
└── assets/                  # Optional: icons or style assets (if any)
```

---

## 🔎 How it Works

* **Time tracking** is handled using `time.time()` and updated every 10ms using `after()`.
* **Lap times** are calculated relative to the last recorded lap.
* **Dark/light themes** are toggled using `ctk.set_appearance_mode()`.
* All components are placed inside a **grid layout** and **resized dynamically**.

---

## 🎨 UI Preview

![image alt](https://github.com/GITWithAkshay/PRODIGY_AD_03/blob/f00d1fc60387954ea736663edf11aa3e9c8781cb/Screenshot%20(183).png)
![image alt](https://github.com/GITWithAkshay/PRODIGY_AD_03/blob/f00d1fc60387954ea736663edf11aa3e9c8781cb/Screenshot%20(189).png)

---

## 🧠 Future Enhancements

* [ ] Save laps to CSV or JSON
* [ ] Keyboard shortcuts (e.g., Space to Start/Pause)
* [ ] Timer mode with countdown and alarms
* [ ] Sound notifications

---

## 📜 License

Feel free to use, modify, and distribute.

---

## 🙏 Acknowledgements

* 🧩 **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** – for providing a modern and intuitive way to design GUI in Python
* 📅 **[Tkcalendar](https://github.com/j4321/tkcalendar)** – for the simple and effective date-picker widget
* 🧠 Python Community – for rich documentation and endless support

Special thanks to the open-source contributors who maintain these projects and to anyone who uses or improves upon this app 🙌

---
