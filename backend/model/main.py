import sys
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
X = y = []
OS = ""
if sys.platform == "win32":
    OS = "windows"
elif sys.platform == "linux":
    OS = "linux"
elif sys.platform == "darwin":
    OS = "mac"
else:
    print("The Operating System of your device is currently not supported. I am sorry")
with open("data.json", "r") as file:
    data = json.load(file)
    for entry in data:
        output_command = entry["output"][OS]
        for variant in entry["input"]:
            X.append(variant)
            y.append(output_command)
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)
while True:
    user_input = sys.argv[1]
    if user_input != None:
        if user_input.lower() in ["exit", "quit", "bye", "go off", "goodbye"]:
            print("Bye")
            break
        else:
            user_vec = vectorizer.transform([user_input])
            predicted_command = model.predict(user_vec)[0]
            print(f"Understood the command: {predicted_command}")
    else:
        print("Please provide a proper command")
