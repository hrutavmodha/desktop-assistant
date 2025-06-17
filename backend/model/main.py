def main():
    import speech_recognition as sr
    import pyttsx3
    from model1.inference import execShellCMD
    from model2.inference import execDynamicCMD
    from model4.inference import getModel
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    with sr.Microphone() as source:
        engine.say("Please say your command")
        engine.runAndWait()
        print("Please say your command")
        audio = recognizer.listen(source)
    cmd = recognizer.recognize_google(audio)
    engine.say("Command received. Executing it may take a while. Please wait.")
    engine.runAndWait()
    print("Command received. Executing it may take a while. Please wait.")
    model = getModel(cmd)
    if model == "model1":
        execShellCMD(cmd)
    elif model == "model2":
        execDynamicCMD(cmd)
    elif model == "model3":
        print("Model 3 is not yet integrated.")
    else:
        print("Could not determine model.")
if __name__ == "__main__":
    main()