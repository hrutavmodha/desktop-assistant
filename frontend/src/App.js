import React from "react"
export default function App() {
  const handleDownload = () => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/download`, {
      method: "GET",
      header: {
        "Content-type": "application/json",
      }
    }).then((res) => {
      return res.json()
    }).then((data) => {
      console.log(data)
    }).catch((error) => {
      console.log(error)
    }
  }
  return (
    <div className = "container">
      <h1>Voice Assistant</h1>
      <p className = "subtitle">Your offline AI companion</p>
      <button onClick = {handleDownload}>Download for Windows</button>
    </div>
  )
}
