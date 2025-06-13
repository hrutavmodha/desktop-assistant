const bcrypt = require("bcryptjs")
const { signToken } = require("./jwts")
const User = require("../schemas/user")
async function handleSignup(req, res) {
  const { name, email, phone, password } = req.body
  if (!name || !email || !phone || !password) {
    return res.status(400).json({ message: "All fields are required" })
  }
  const existing = await User.findOne({ email })
  if (existing) {
    return res.status(409).json({ message: "User already exists" })
  }
  const hashed = await bcrypt.hash(password, 10)
  const newUser = new User({ name, email, phone, password: hashed })
  await newUser.save()
  const token = signToken({ id: newUser._id })
  res.cookie("token", token, {
    httpOnly: true,
    sameSite: "strict",
    secure: true,
    maxAge: 7 * 24 * 60 * 60 * 1000
  })
  res.status(200).json({ message: "You have signed up successfully" })
}
module.exports = handleSignup
