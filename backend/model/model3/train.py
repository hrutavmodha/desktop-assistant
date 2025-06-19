from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from joblib import dump
import json
import sys
# def removePlaceholders(temp, placeholders):
#     from itertools import product
#     keys = list(placeholders.keys())
#     values = list(placeholders.values())
#     combs = product(*values)
#     res = []
#     for comb in combs:
#         tCopy = temp
#         for key, value in zip(keys, comb):
#             tCopy = tCopy.replace(key, value)
#         res.append(tCopy)
#     return res
with open("backend/model/model3/data.json") as file:
    content = json.load(file)
X, y = [], []
OS = ""
if sys.platform == "win32":
    OS = "windows"
elif sys.platform == "linux":
    OS = "linux"
elif sys.platform == "darwin":
    OS = "mac"
else:
    print("Unsupported OS")
for item in content:
    for sentence in item["input"]:
        # X.extend(removePlaceholders(sentence, {
        #     "<file>": ["test.txt", "resume.pdf", "data.txt", "todo.json","app.exe"], 
        #     "<source>": ["test.txt", "resume.pdf", "data.txt", "todo.json", "app.exe"], 
        #     "<destination>": ["test.txt", "resume.pdf", "data.txt", "todo.json", "app.exe"], 
        #     "<folder>": ["Documents", "Downloads", "Desktop", "Pictures", "Videos", "Music", "frontend", "backend", "model", "C:"]
        # }))
        # y.extend(removePlaceholders(item["output"][OS], {
        #     "<file>": ["test.txt", "resume.pdf", "data.txt", "todo.json","app.exe"], 
        #     "<source>": ["test.txt", "resume.pdf", "data.txt", "todo.json", "app.exe"], 
        #     "<destination>": ["test.txt", "resume.pdf", "data.txt", "todo.json", "app.exe"], 
        #     "<folder>": ["Documents", "Downloads", "Desktop", "Pictures", "Videos", "Music", "frontend", "backend", "model", "C:"]
        # }))
        X.append(sentence)
        y.append(item["output"][OS])
model = MultinomialNB()
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = model.fit(X_vec, y)
dump(model, "backend/model/model3/model3.pkl")
dump(vectorizer, "backend/model/model3/vectorizer3.pkl")
print("Model-3 and vectorizer-3 are saved successfully")