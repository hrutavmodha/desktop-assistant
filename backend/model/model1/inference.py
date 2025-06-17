def execShellCMD(cmd):
  from joblib import load
  import os, sys
  # basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
  # modelFolder = os.path.join(basePath, "backend", "model", "model1")
  # modelPath = os.path.join(modelFolder, "model.pkl") 
  # vectorizerPath = os.path.join(modelFolder, "vectorizer.pkl")
  model = load("backend/model/model4/model.pkl")
  vectorizer = load("backend/model/model4/vectorizer.pkl")
  user_vec = vectorizer.transform([cmd])
  predicted_command = model.predict(user_vec)[0]
  print(f"Understood your command. Processing it, it may take few moment. Please wait.")
  os.system(predicted_command)