def main(cmd):
    from backend.model.model1.inference import execShellCMD
    from backend.model.model2.inference import execDynamicCMD
    from backend.model.model4.inference import getModel
    model = getModel(cmd)
    res = ""
    if model == "model1":
        res = execShellCMD(cmd)
    elif model == "model2":
        res = execDynamicCMD(cmd)
    elif model == "model3":
        res = "Model 3 is not yet integrated."
    else:
        res = "Could not determine model."
    return res