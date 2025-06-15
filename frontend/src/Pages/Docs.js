import { H1 } from "../Components/Heading"
import P from "../Components/Paragraph"
export default function Documentation() {
    return (
        <div className="max-w-3xl mx-auto py-10 px-4 space-y-6">
            <H1>Documentation</H1>
            <P>
                The Smart Voice Assistant is structured around modular machine learning models:
                <ul className="list-disc list-inside pl-4 mt-2">
                    <li><strong>Model 1:</strong> Command-to-action (shell tasks)</li>
                    <li><strong>Model 2:</strong> Dynamic query handling (search, Wikipedia)</li>
                    <li><strong>Model 4:</strong> Router that classifies and routes queries to relevant models</li>
                </ul>
            </P>
            <P>
                <strong>Getting Started:</strong><br />
                1. Download your OS-specific executable from the <a className="text-blue-600 underline" href="/">here</a><br />
                2. Run it. First time launch will auto-download necessary models.<br />
                3. Use the "Give Command" button to speak your query.
            </P>
            <P>
                For full API details and contribution guidelines, check out <a className="text-blue-600 underline" href="https://github.com/hrutavmodha/voice-assistant" target="_blank" rel="noreferrer"> My GitHub repository</a>
            </P>
        </div>
    );
}
