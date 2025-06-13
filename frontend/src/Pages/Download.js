import { H1 } from "./Components/Headings"
import Button from "./Components/Button"
export default function Download() {
  const handleDownload = () => {
    window.location.href = `${process.env.REACT_APP_BACKEND_URL}/download`
  }
  return (
    <>
      <H1>Voice Assistant</h1>
      <p>Download the Voice-Assistant application for your OS from the given below "Download" button.</p>
      <Button onClick={handleDownload}>Download</button>
    </>
  )
}
