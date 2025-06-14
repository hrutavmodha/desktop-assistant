import { Link } from "react-router-dom"
import { H3 } from "./Components/Headings"
export default function NavBar() {
    return (
        <nav className="bg-gray-800 text-white px-6 py-4 shadow-md">
            <div className="max-w-6xl mx-auto flex justify-between items-center">
                <H3>Smart Voice Assistant</H3>
                <div>
                    <Link to="/" className="text-white hover:text-yellow-400 transition-colors duration-200">
                        Download
                    </Link>
                    <Link to="/about" className="text-white hover:text-yellow-400 transition-colors duration-200">
                        About
                    </Link>
                    <Link to="/contact" className="text-white hover:text-yellow-400 transition-colors duration-200">
                        Contact
                    </Link>
                    <Link to="/documentation" className="text-white hover:text-yellow-400 transition-colors duration-200">
                        Documentation
                    </Link>
                    <Link to="/signup" className="text-white hover:text-yellow-400 transition-colors duration-200">
                        Sign Up
                    </Link>
                </div>
            </div>
        </nav>
    )
}
