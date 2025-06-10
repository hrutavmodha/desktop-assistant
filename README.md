# 🧠 Voice-Assistant

- Voice-Assistant is a **ML-based Voice Assistant**

- This is a desktop-based voice assistant powered by the ML model, which is built using Python.

- The UI is built using Electron.js while inference is done by using Node.js.
  
- It understands your speech, processes it using a custom-trained intent recognition model and executes platform-specific commands.

---

# 🚀 Features

- 🎙️ Voice Input
  
- 🤖 ML-based Intent Detection
  
- ⚙️ Cross-platform Command Execution

- 🗣️ Voice Output

- 🖥️ Desktop-first App

- 🔐 Privacy-Focused

---

# 🏗️ Tech Stack

| Layer         | Stack                             |
|---------------|------------------------------------|
| Frontend      | HTML, CSS, JS and React.js            |
| Backend       | Node.js and Python |
| Desktop UI | Electron.js               |
| Model         | Light-weight ML model |
| Voice I/O       | Web Speech API         |

---

# 🧠 How It Works

1. 🎙️ User speaks a command

2. 🎧 Voice is transcribed and sent to Python backend

3. 🧠 The ML model classifies intent

4. 💻 Executes the platform-specific command

5. 🗣️ Response is spoken back to the user alongwith the execution of the task

---

# 🔁 Requirements

- Node.js & npm

- Python & pip

- Electron.js & React

---

# 🛠️ Run Locally

## 1. Clone the repository

```Bash
git clone "https://github.com/hrutavmodha/voice-assistant.git"
cd ./voice-assistant
```

## 2. Start the training

```Bash
cd ./backend/model/
python ./main.py
```

## 3. Install dependencies

```Bash
cd ..
npm install
pip install sklearn
cd ../frontend
npm install
cd ..
npm install
cd backend
```

## 4. Start the server

```Bash
npm run start
```

---

# 👨‍💻 Author

Made with passion by **Hrutav Modha**

---

# 📌 Note

- This project is purely offline and does **not rely on any of the external APIs and nor it is dumb `if-elif-else`-like rule-based voice-assistant**

- It’s a fully local voice assistant with a custom-trained AI model, which is designed with keeping privacy in mind.
