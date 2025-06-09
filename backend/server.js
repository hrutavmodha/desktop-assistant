const express = require("express")
const cors = require("cors")
const path = require("path")
require("dotenv").config()
const app = express()
app.use(cors({
  origin: process.env.REACT_APP_FRONTEND_URL
}))
app.get("/download", (req, res) => {
    const file = path.join(__dirname, "dist")
    res.download(file, "VoiceAssistant.exe", (error) => {
        if (error) {
            console.log(error)
            res.status(500).send("Internal server error. Please try again later")
        }
    })
})
const PORT = process.env.PORT || 5000
app.listen(PORT, () => {
    console.log(`Download Server running on port ${PORT}`)
})
