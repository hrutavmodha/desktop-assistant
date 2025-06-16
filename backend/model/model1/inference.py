def execShellCMD(cmd):
  from joblib import load
  import os
  model = load("model1/model.pkl")
  vectorizer = load("model1/vectorizer.pkl")
  user_vec = vectorizer.transform([cmd])
  predicted_command = model.predict(user_vec)[0]
  print(f"Understood your command. Processing it, it may take few moment. Please wait.")
  os.system(predicted_command)
