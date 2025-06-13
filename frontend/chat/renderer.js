const { execFile } = require("child_process")
const os = require("os")
const path = require("path")
const startBtn = document.getElementById("startBtn")
const convoBox = document.getElementById("convoBox")
const platform = os.platform()
let filename = "" 
  switch (platform) {
    case platform === "win32":
      filename = "voice_assistant_windows-latest.exe"
      break
    case platform === "darwin":
      filename = "voice_assistant_macos-latest"
      break
    case platform === "linux":
      filename = "voice_assistant_ubuntu-latest"
      break
    default:
      console.log("Unsupported")
  }
const exePath = path.join(os.homedir(), filename);
startBtn.addEventListener("click", () => {
  const recognition = new window.webkitSpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.start();
  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    appendToConvo("You: ", transcript);
    execFile(exePath, [transcript], (err, stdout, stderr) => {
      if (err || stderr) {
        const errMsg = err?.message || stderr;
        appendToConvo("Error: ", errMsg);
        return;
      }
      const response = stdout.trim();
      appendToConvo("Bot: ", response);
      const synth = window.speechSynthesis;
      const utter = new SpeechSynthesisUtterance(response);
      synth.speak(utter);
    });
  };
  recognition.onerror = (e) => {
    appendToConvo("Error", e.error);
  };
});
function appendToConvo(sender, message) {
  const para = document.createElement("p");
  para.innerHTML = `<h4>${sender}:</h4> ${message}`;
  convoBox.appendChild(para);
  convoBox.scrollTop = convoBox.scrollHeight;
}
