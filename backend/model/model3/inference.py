def execFileCMD():
    import sys
    from subprocess import getoutput as run
    from joblib import load
    cmd = sys.argv[1]
    model = load("backend/model/model3/model3.pkl")
    vectorizer = load("backend/model/model3/vectorizer3.pkl")
    words = cmd.split(" ")
    newcmd = ""
    print(words)
    file = ""
    for i in range(len(words)): 
        if "." in words[i]:
            file = words[i]
            words[i] = "<file>"
    for i in words:
        newcmd = newcmd + " " + i
    print(newcmd)
    cmd_vec = vectorizer.transform([newcmd])
    result = model.predict(cmd_vec)[0]
    result = result.split(" ")
    for i in range(len(result)):
        if result[i] == "<file>":
            result[i] = file
    run(result)
if __name__ == "__main__":
    execFileCMD()