# 🧠 Voice-GPT - 
## An Offline Transformer-based Voice Assistant

Voice-GPT is a fully offline, desktop-based voice assistant powered by a fine-tuned transformer model — built using Python, ElectronJS, and NodeJS. It understands your speech, processes it using a custom-trained intent recognition model, and executes platform-specific commands — all without requiring an internet connection.

---

## 🚀 Features

- 🎙️ **Voice Input (Speech Recognition)**
  
- 🤖 **Transformer-based Intent Detection (HuggingFace)**
  
- ⚙️ **Cross-platform Command Execution (Windows/Linux/Mac)**  

- 🗣️ **Voice Output (Text-to-Speech)**  

- 🖥️ **Desktop GUI (Electron)**  

- 🔐 **100% Offline – Privacy-Focused**

---

## 🏗️ Tech Stack

| Layer         | Stack                             |
|---------------|------------------------------------|
| Frontend      | HTML, CSS, Vanilla JS              |
| Backend       | Python, PyTorch, HuggingFace, OS   |
| Desktop Shell | ElectronJS, NodeJS                 |
| Model         | Transformer-based Intent Classifier|
| Speech        | Web Speech API / pyttsx3           |

---

## 🧠 How It Works

1. 🎙️ User speaks a command

2. 🎧 Voice is transcribed → sent to Python backend

3. 🧠 Transformer model classifies intent

4. 💻 Executes mapped platform-specific command

5. 🗣️ Response is spoken back to the user

---

## 🔧 Setup & Run

**🔁 Requirements**

- Node.js & npm

- Python & pip

- Electron.js & React

### 🛠️ Run Locally

**1. Clone the repository**

```Bash
git clone "https://github.com/hrutavmodha/voice-assistant.git"
cd ./voice-assistant
```

**2. Start the training**

**⚠️ NOTE: For training the model locally, make sure that you have dedicated CUDA GPU with 6GB VRAM and PC RAM 8-16GB, else you can use Google Colab or Kaggle**

```Bash
cd ./backend/model/
python ./train.py        
python ./inference.py "Open Google"
```

**3. Install dependencies**

```Bash
cd ..
npm install
cd ../frontend
npm install
cd ..
npm install
```

**4. Start the server**

```Bash
npm run start
```

---

## 👨‍💻 Author

Made with passion by Hrutav Modha

---

## 📌 Note

- This project is purely offline and does not rely on **any of the external APIs** like OpenAI or Google Assistant, **nor it is dumb `if-elif-else`-like rule-based voice-assistant**

- It’s a fully local voice assistant with a custom-trained AI model — designed with privacy and hackability in mind.
