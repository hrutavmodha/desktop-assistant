const startBtn = document.getElementById("startBtn")
const convoBox = document.getElementById("convoBox")
startBtn.addEventListener("click", () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.start();
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        appendToConvo("You", transcript);
        window.python.run(transcript)
        const response = stdout.trim();
        appendToConvo("Bot", response);
        const synth = window.speechSynthesis;
        const utter = new SpeechSynthesisUtterance(response);
        synth.speak(utter)
    }
    recognition.onerror = (e) => {
        appendToConvo("Error", e.error);
    }
})
function appendToConvo(sender, message) {
    const para = document.createElement("div");
    para.innerHTML = `<h4>${sender}:</h4> ${message}`;
    convoBox.appendChild(para);
    convoBox.scrollTop = convoBox.scrollHeight;
}