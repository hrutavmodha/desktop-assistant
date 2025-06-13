import { H1 } from "../Components/Headings"
import P from "../Components/Paragraph"
export default function Contact() {
  return (
    <div className="max-w-2xl mx-auto py-10 px-4 space-y-6">
      <H1>Contact Us</H1>
      <P>
        Have questions, suggestions, or want 
        to report a bug? I’d 
        love to hear from you. 
        Drop me an email.
      </P>
      <P>
        <strong>Email:</strong> <a href="mailto:modhahrutav@gmail.com" className="text-blue-600 underline">modhahrutav@gmail.com</a><br />
        <strong>GitHub Issues:</strong> <a href="https://github.com/hrutavmodha/voice-assistant/issues" className="text-blue-600 underline">Report Here</a>
      </P>
      <P>
        We aim to respond to all messages within 48 hours. For faster help, describe your environment (OS, command tried, error shown).
      </P>
    </div>
  )
}
