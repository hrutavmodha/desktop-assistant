const startBtn = document.getElementById("startBtn")
const userText = document.getElementById("userText")
const botReply = document.getElementById("botReply")
startBtn.addEventListener("click", async () => {
  const { exec } = require("child_process")
  await exec(`python ../../backend/model/inference.py ${userText}`, (err, stdout, stderr) => {
    if (err) {
      botReply.innerText = "Error occurred"
      console.log(err)
      return
    }
    userText.innerText = "Open YouTube"
    botReply.innerText = stdout.trim()
  })
})
