def execShellCMD(cmd):
  from joblib import load
  import os, sys
  basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
  modelFolder = os.path.join(basePath, "backend", "model", "model4")
  modelPath = os.path.join(modelFolder, "model1.pkl") 
  vectorizerPath = os.path.join(modelFolder, "vectorizer1.pkl")
  model = load(modelPath)
  vectorizer = load(vectorizerPath)
  user_vec = vectorizer.transform([cmd])
  predicted_command = model.predict(user_vec)[0]
  print(f"Understood your command. Processing it, it may take few moment. Please wait.")
  os.system(predicted_command)