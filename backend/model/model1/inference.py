def execShellCMD(cmd):
  from joblib import load
  from subprocess import getoutput as run
  # basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
  # modelFolder = os.path.join(basePath, "backend", "model", "model1")
  # modelPath = os.path.join(modelFolder, "model.pkl") 
  # vectorizerPath = os.path.join(modelFolder, "vectorizer.pkl")
  model = load("backend/model/model1/model.pkl")
  vectorizer = load("backend/model/model1/vectorizer.pkl")
  user_vec = vectorizer.transform([cmd])
  predicted_command = model.predict(user_vec)[0]
  res = run(predicted_command)
  return "Your command has been executed successfully. It may take a few moments to see changes on the screen. Please wait for a while!" if res is None else res