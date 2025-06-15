import { H1, H2 } from "../Components/Heading"
import Button from "../Components/Button"
import P from "../Components/Paragraph"
export default function Download() {
    const handleDownload = () => {
        window.location.href = `${process.env.REACT_APP_BACKEND_URL}/download`
    }
    return (
        <div className="max-w-3xl mx-auto py-10 px-4 space-y-6">
            <H1>Voice Assistant</H1>
            <P>Download the Voice-Assistant application for your OS from the given below "Download" button.</P>
            <H2> Download the Smart Voice Assistant</H2>
            <P>Our cross-platform Smart Voice Assistant brings AI directly to your desktop — offering intelligent responses, natural language interactions, and seamless offline capabilities. Whether you're looking to launch applications, ask questions, perform local system tasks, or handle real-time queries — this assistant can help you do it all with just your voice.</P>

            <H2> Key Features:</H2>
            <ol className="mx-5" type="1">
                <li>Voice-activated commands with intelligent model routing</li>
                <li>Offline support for running shell commands securely</li>
                <li>Dynamic query handling (Search, Wikipedia, etc.)</li>
                <li>Privacy-first: No cloud sync, no user data tracking</li>
                <li>Lightweight and responsive desktop experience</li>
            </ol>
            <P>Choose your platform and click the download button below to get started.</P>
            <Button onClick={handleDownload}>Download</Button>
        </div>
    )
}