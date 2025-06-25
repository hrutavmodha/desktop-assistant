def main():
    import sys
    from backend.model.model1.inference import execShellCMD
    from backend.model.model2.inference import execDynamicCMD
    from backend.model.model4.inference import getModel
    from backend.model.model3.inference import execFileCMD
    from backend.model.memory import Memory
    cmd = sys.argv[1]
    model = getModel(cmd)
    mind = Memory()
    res = ""
    if model == "model1":
        res = execShellCMD(cmd)
    elif model == "model2":
        res = execDynamicCMD(cmd)
    elif model == "model3":
        res = execFileCMD(cmd)
    else:
        res = "Could not determine model."
    mind.writeInFile(cmd, res)
    return res
if __name__ == "__main__":
    main()