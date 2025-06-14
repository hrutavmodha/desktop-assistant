import { useState } from "react"
import Input from "../Components/Input"
import Button from "../Components/Button"
import P from "../Components/Paragraph"
import { H1 } from "../Components/Headings"
export default function SignUp() {
  const [form, setForm] = useState({ 
    name: "", 
    email: "", 
    phone: "", 
    password: "" 
  })
  const [status, setStatus] = useState("")
  const handleChange = (e) => {
    setForm({ 
      ...form, 
      [e.target.name]: e.target.value 
    })
  }
  const handleSubmit = (e) => {
    e.preventDefault()
    if (!form.name.trim() || 
        !form.email.trim() || 
        !form.phone.trim() || 
        !form.password.trim()) {
  setStatus("Please fill all fields.")
    } else {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/signup`, {
      method: "POST",
      headers: { 
        "Content-Type": "application/json"
      },
      credentials: "include",
      body: JSON.stringify(form),
    }).then((res) => {
      return res.json()
    }).then((data) => {
      setStatus(data.message)
    }).catch(err => {
      setStatus("Server error. Try again.")
      console.log(err)
    })
  }
  }
  return (
    <div className="max-w-md mx-auto mt-10 p-4 border rounded-xl shadow-lg">
      <H1>Sign Up</H1>
      <form className="space-y-4 mt-4">
        <Input placeholder="Name" name="name" value={form.name} onChange={handleChange} />
        <Input placeholder="Email" name="email" type="email" value={form.email} onChange={handleChange} />
        <Input placeholder="Phone" name="phone" type="tel" value={form.phone} onChange={handleChange} />
        <Input placeholder="Password" name="password" type="password" value={form.password} onChange={handleChange} />
        <Button onClick={handleSubmit}>Sign Up</Button>
        { status !== "" 
          ? <P>{status}</P>
          : null }
      </form>
    </div>
  )
}
