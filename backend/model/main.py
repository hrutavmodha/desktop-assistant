import sys
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from handlers.searchGoogle import searchGoogle
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
    match = re.search(r"(?:search|look\s*up|google)\s+(.*)", user_input, flags = re.I)
    if user_input.lower() in ["exit", "quit", "bye", "go off", "goodbye"]:
        print("Bye")
        break
    elif match:
        query = match.group(1)
        searchGoogle(query)
    else:
        user_vec = vectorizer.transform([user_input])
        predicted_command = model.predict(user_vec)[0]
        print("Understood your command. Processing it, it may take few moment. Please wait")
        os.system(predicted_command)
