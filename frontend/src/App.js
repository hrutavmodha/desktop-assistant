import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Home from "./Components/Home"
import Download from "./components/Download"
import Docs from "./Components/Docs"
export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/download" element={<Download />} />
        <Route path="/docs" element={<Docs />} />
      </Routes>
    </Router>
  )
}
