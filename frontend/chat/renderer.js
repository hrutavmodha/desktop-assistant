const startBtn = document.getElementById("startBtn")
const userText = document.getElementById("userText")
const botReply = document.getElementById("botReply")
startBtn.addEventListener("click", async () => {
  const { exec } = require("child_process")
  exec(`python ../../backend/model/inference.py ${userText.innerText}`, (err, stdout, stderr) => {
    if (err) {
      botReply.innerText = "Error occurred"
      console.log(err)
      return
    }
    botReply.innerText = stdout.trim()
  })
})
