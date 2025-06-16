def main():
    log = print
    import sys
    from model1.inference import execShellCMD
    from model2.inference import execDynamicCMD
    from model4.inference import getModel
    log("All model inferences imported successfully")
    if len(sys.argv) < 2:
        log("No command provided!")
        return
    cmd = sys.argv[1].lower()
    model = getModel(cmd)
    log("Command sent to model 4 for classification of your command")
    if model == "model1":
        execShellCMD(cmd)
        log("Condition 1 matched")
    elif model == "model2":
        execDynamicCMD(cmd)
        log("Condition 2 matched")
    elif model == "model3":
        print("Model 3 is not yet integrated.")
        log("Condition 3 matched")
    else:
        print("Could not determine model.")
        log("No condition matched")
if __name__ == "__main__":
    main()