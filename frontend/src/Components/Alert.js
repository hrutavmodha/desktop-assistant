import { useEffect, useState } from "react"
export default function Alert({ message, type="info", duration=3000 }) {
  const [visible, setVisible] = useState(true)
  useEffect(() => {
    const timer = setTimeout(() => {
      setVisible(false)
    }, duration)
    return () => {
      clearTimeout(timer)
    }
  }, [duration])
  if (!visible) 
    return null
  const colorMap = {
    info: "bg-blue-100 text-blue-800 border-blue-300",
    success: "bg-green-100 text-green-800 border-green-300",
    error: "bg-red-100 text-red-800 border-red-300",
    warning: "bg-yellow-100 text-yellow-800 border-yellow-300"
  }
  return (
    <div className={`border-l-4 p-4 rounded-md shadow-md mb-4 transition-opacity duration-500 ${colorMap[type]}`}>
      <p className="text-sm font-medium">{message}</p>
    </div>
  )
}
