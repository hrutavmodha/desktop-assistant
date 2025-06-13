import { Link } from "react-router-dom"
import { H1 } from "./Components/Headings"
export default function Navbar() {
    return (
        <nav className="bg-gray-800 text-white px-6 py-4 shadow-md">
            <div className="max-w-6xl mx-auto flex justify-between items-center">
                <H1>Smart Voice Assistant</H1>
                <div>
                    <Link to="/" className="text-white hover:text-yellow-400 transition-colors duration-200">
                        Download
                    </Link>
                </div>
            </div>
        </nav>
    )
}
