import { useState } from "react"
import Input from "../Components/Input"
import Button from "../Components/Button"
import P from "../Components/Paragraph"
export default function Login() {
  const [formData, setFormData] = useState({
    email: "",
    phone: "",
    password: "",
  })
  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev, 
      [name]: value 
    }))
  }
  const handleSubmit = (e) => {
    e.preventDefault()
    if (!formData.email || 
        !formData.phone || 
        !formData.password) {
      alert("All fields are required")
      return
    }
    fetch(`${process.env.REACT_APP_BACKEND_URL}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    }).then((res) => {
      return res.json()
    }).then((data) => {
      alert(data.message)
    })
    .catch((err) => {
      console.error(err)
      alert("Login failed")
    })
  }
  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-2xl shadow-lg">
      <P className="text-2xl font-bold mb-4">Sign In to your Account</P>
      <form className="space-y-4">
        <Input
          placeholder="Email"
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        <Input
          placeholder="Phone"
          type="text"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
        />
        <Input
          placeholder="Password"
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
        <Button onClick={handleSubmit}>
        </Button>
      </form>
    </div>
  )
}
