const express = require("express")
const cors = require("cors")
const path = require("path")
const { handleSignup } = require("./middlewares/auth")
const { handleDownload } = require("./middlewares/download")
const connect = require("./connect")
require("dotenv").config()
const app = express()
app.use(express.json())
app.use(cors({
  origin: process.env.REACT_APP_FRONTEND_URL,
  credentials: true,
}))
connect("voice-assistant")
app.get("/download", handleDownload)
app.post("/signup", handleSignup)
app.listen(process.env.PORT, () => {
    console.log(`Server running on port ${process.env.PORT}`)
})
