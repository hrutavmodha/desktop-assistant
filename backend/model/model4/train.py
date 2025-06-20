import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
with open("backend/model/model4/data.json") as f:
    data = json.load(f)
X, y = [], []
for item in data:
    for sentence in item["input"]:
        X.append(sentence.lower())
        y.append(item["output"])
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
clf = LogisticRegression()
clf.fit(X_vec, y)
dump(clf, "backend/model/model4/model4.pkl")
dump(vectorizer, "backend/model/model4/vectorizer4.pkl")
print("Model-4 and vectorizer-4 are saved successfully")