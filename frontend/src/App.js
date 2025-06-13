import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Download from "./Pages/Download"
export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Download/>} />
        <Route>
      </Routes>
    </Router>
  )
}
