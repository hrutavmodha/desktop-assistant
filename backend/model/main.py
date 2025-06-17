def main(cmd):
    from backend.model.model1.inference import execShellCMD
    from backend.model.model2.inference import execDynamicCMD
    from backend.model.model4.inference import getModel
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