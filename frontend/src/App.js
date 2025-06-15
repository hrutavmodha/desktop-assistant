import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Download from "./Pages/Download"
import About from "./Pages/About"
import Contact from "./Pages/Contact"
import Documentation from "./Pages/Docs"
import SignUp from "./Pages/SignUp"
import NavBar from "./Components/NavBar"
import "./index.css"
export default function App() {
  return (
    <Router className="overflow-none">
      <NavBar/>
      <Routes>
        <Route path="/" element={<Download/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/contact" element={<Contact/>}/>
        <Route path="/documentation" element={<Documentation/>}/>
        <Route path="/signup" element={<SignUp/>}/>
      </Routes>
    </Router>
  )
}
