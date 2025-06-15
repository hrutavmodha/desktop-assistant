import { Link } from "react-router-dom"
import { H3 } from "./Heading"
export default function NavBar() {
    return (
        <nav className="bg-gray-800 text-white px-3 py-2 shadow-md sticky top-0">
            <div className="max-w-6xl mx-auto flex justify-between items-center">
                <H3>Smart Voice Assistant</H3>
                <div className="flex justify-around items-center">
                    <Link to="/" className="text-white hover:text-yellow-400 transition-colors duration-200 mx-[10px]">
                        <button>Download</button>
                    </Link>
                    <Link to="/about" className="text-white hover:text-yellow-400 transition-colors duration-200 m-[10px]">
                        <button>About</button>
                    </Link>
                    <Link to="/contact" className="text-white hover:text-yellow-400 transition-colors duration-200 m-[10px]">
                        <button>Contact</button>
                    </Link>
                    <Link to="/documentation" className="text-white hover:text-yellow-400 transition-colors duration-200  m-[10px] ">
                        <button>Documentation</button>
                    </Link>
                    <Link to="/signup" className="text-white hover:text-yellow-400 transition-colors duration-200  m-[10px]">
                        <button>Sign Up</button>
                    </Link>
                </div>
            </div>
        </nav>
    )
}
