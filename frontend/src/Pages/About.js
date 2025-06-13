import { H1 } from "../Components/Headings"
import P from "../Components/Paragraph"
export default function About() {
  return (
    <div className="max-w-3xl mx-auto py-10 px-4 space-y-6">
      <H1>About Smart Voice Assistant</H1>
      <P>
        The Smart Voice Assistant is 
        an open-source, privacy
        -focused desktop application built to
        help you perform everyday tasks
        using just your voice. 
        Whether it's opening apps
        , fetching information from the web
        , or managing files — 
        our assistant does it all 
        without sending your data to 
        external servers.
      </P>
      <P>
        Designed for speed, minimalism
        , and offline-first capabilities
        , this assistant runs locally 
        on your system and is 
        fully extendable. It works 
        seamlessly across Windows, Linux, 
        and macOS, and supports both
        command and natural language-based 
        interactions.
      </P>
      <P>
        Born from the need to 
        build a voice-based productivity 
        tool that respects privacy, this 
        project is now community-driven 
        and constantly evolving. We invite
        developers, designers, and privacy 
        advocates to contribute and shape 
        the future of intelligent assistants.
      </P>
    </div>
  );
}
