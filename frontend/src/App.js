import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Download from "./Pages/Download"
import About from "./Pages/About"
import Contact from "./Pages/Contact"
import Documentation from "./Pages/Docs"
import Signup from "./Pages/Signup"
import NavBar from "./Components/NavBar"
export default function App() {
  return (
    <Router>
      <NavBar/>
      <Routes>
        <Route path="/" element={<Download/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/contact" element={<Contact/>}/>
        <Route path="/documentation" element={<Documentation/>}/>
        <Route path="/signup" element={<Signup/>}/>
      </Routes>
    </Router>
  )
}
