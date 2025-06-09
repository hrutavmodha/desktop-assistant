import React from "react"
export default function App() {
  const handleDownload = () => {
    window.location.href = `${process.env.REACT_APP_BACKEND}/download`
  }
  return (
    <div className = "container">
      <h1>Voice Assistant</h1>
      <p className = "subtitle">Your offline AI companion</p>
      <button onClick = {handleDownload}>Download for Windows</button>
    </div>
  )
}
