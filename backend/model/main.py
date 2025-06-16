def main():
    import sys
    from model1.inference import execShellCMD
    from model2.inference import execDynamicCMD
    from model4.inference import getModel
    if len(sys.argv) < 2:
        print("No command provided!")
        return
    cmd = sys.argv[1].lower()
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