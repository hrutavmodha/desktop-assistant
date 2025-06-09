
# 🤝 Contributing to VoiceGPT

Hello! 👋 Thank you for your interest in contributing to VoiceGPT — an open-source offline voice assistant powered by Transformers and NodeJS/Electron.

---

# 🧠 What's Inside This Project

- 🎙️ Voice Input via Web Speech API
- 🤖 Intent Recognition using Transformers (HuggingFace)
- 🗣️ Speech Output using SpeechSynthesis
- ⚙️ OS Command Execution (Windows, Linux, Mac)
- 🖥️ Electron GUI + NodeJS Bridge
- 🔐 100% Offline Architecture

---

# 📌 Contribution Guidelines

## ✅ You Can Contribute In:

- Improving **training data quality** (`data.json`)
- Adding new **command intents + variations**
- Enhancing **frontend UI/UX**
- Adding **new OS-level automations**
- Bug fixes and performance improvements
- Writing **tests**, optimization scripts or installation setup
- Adding **new platform support**

---

## 🛠️ Setup Instructions

**1. *Fork* this repository**

**2. Clone it locally**
   ```bash
   git clone "https://github.com/<your-username>/voice-assistant.git"
   ```

**3. Install dependencies**

**i. Root**

```Bash
cd voice-assistant
npm install
```

**ii. Frontend**

```Bash
cd frontend
npm install
```

**iii. Backend**

```Bash
cd backend/model
pip install transformers pytorch sys
python train.py
```

**4. ✅ Start contributing**

---

## 💡 Code Style Guidelines

1. Use clear, modular code

2. JS: ES6+ preferred (const, let, arrow functions)

3. Python: Follow PEP8

4. Use meaningful commit messages

---

## 🧪 Testing Your Contributions

1. Try multiple voice inputs

2. Validate JSON format

3. Console output should be clean

4. Test on at least one OS.

---

## 🚀 Submitting a Pull Request

1. Push your changes to your fork

2. Open a pull request (PR) to main branch

3. Describe your changes clearly

4. Link any related issues (if any)

5. Wait for review and merge 🎉
