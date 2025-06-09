const { exec } = require("child_process")
const startBtn = document.getElementById("startBtn")
const userText = document.getElementById("userText")
const botReply = document.getElementById("botReply")
startBtn.addEventListener("click", async () => {
  const recognition = new window.webkitSpeechRecognition()
  recognition.lang = "en-US"
  recognition.interimResults = false
  recognition.start()
  recognition.onresult = function (event) {
    const transcript = event.results[0][0].transcript
    userText.innerText = transcript
    exec(`python ../../backend/model/inference.py "${transcript}"`, (err, stdout, stderr) => {
      if (err) {
        botReply.innerText = "Error occurred"
        console.log(err)
        return
      }
      const response = stdout.trim()
      botReply.innerText = response
      const synth = window.speechSynthesis
      const utter = new SpeechSynthesisUtterance(response)
      synth.speak(utter)
    })
  }
  recognition.onerror = function (event) {
    botReply.innerText = "Voice input failed"
    console.error(event.error)
  }
})
