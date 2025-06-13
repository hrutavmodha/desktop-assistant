import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Download from "./Pages/Download"
import About from "./Pages/About"
import NavBar from "./Componente/NavBar"
export default function App() {
  return (
    <Router>
      <NavBar/>
      <Routes>
        <Route path="/" element={<Download/>}/>
        <Route path="/about" element={<About/>}/>
      </Routes>
    </Router>
  )
}
