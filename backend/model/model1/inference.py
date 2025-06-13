def execShellCMD(cmd):
  from joblib import load
  import sys
  import os
  model = load("backend/model/model1/model.pkl")
  vectorizer = load("backend/model/model1/vectorizer.pkl")
  user_vec = vectorizer.transform([cmd])
  predicted_command = model.predict(user_vec)[0]
  print(f"Understood your command. Processing it, it may take few moment. Please wait.")
