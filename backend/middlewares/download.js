module.exports = handleDownload(req, res) => {
    const file = path.join(__dirname, "dist")
    res.download(file, "VoiceAssistant.exe", (error) => {
        if (error) {
            console.log(error)
            res.status(500).send("Internal server error. Please try again later")
        }
    })
 }
