#def execShellCMD():
from joblib import load
import sys
import os
model = load("backend/model/model1/model.pkl")
vectorizer = load("backend/model/model1/vectorizer.pkl")
user_input = sys.argv[1].lower()
user_vec = vectorizer.transform([user_input])
predicted_command = model.predict(user_vec)[0]
print(f"Understood your command. Processing it, it may take few moment. Please wait. This is predicted command: {predicted_command}")
