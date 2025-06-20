def execFileCMD(cmd):
    def openFile(path):
        import sys
        import subprocess
        # basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
        # modelFolder = os.path.join(basePath, "backend", "model", "model3")
        # modelPath = os.path.join(modelFolder, "model3.pkl")
        # vectorizerPath = os.path.join(modelFolder, "vectorizer3.pkl")
        OS = sys.platform
        if OS == "win32":
            subprocess.call(["explorer", "/select", f'"{path}"'])
        elif OS == "linux":
            subprocess.call(["xdg-open", path])
        elif OS == "darwin":
            subprocess.call(["open", path])
        else:
            return "Unsupported Operating System"
    from subprocess import getoutput as run
    from joblib import load
    model = load("backend/model/model3/model3.pkl")
    vectorizer = load("backend/model/model3/vectorizer3.pkl")
    words = cmd.split(" ")
    newcmd = ""
    file = ""
    for i in range(len(words)): 
        if "." in words[i]:
            file = words[i]
            words[i] = "<file>"
    for i in words:
        newcmd = newcmd + " " + i
    cmd_vec = vectorizer.transform([newcmd])
    result = model.predict(cmd_vec)[0]
    result = result.split(" ")
    for i in range(len(result)):
        if result[i] == "<file>":
            result[i] = file
    res = run(result)
    openFile(file)
    return res if res is not None else result