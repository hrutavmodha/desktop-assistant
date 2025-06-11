from json import load
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump as save
with open("data.json") as file:
    data = load(file)
X, y = [], []
for entry in data:
    for sentence in entry["input"]:
        X.append(sentence.lower())
        y.append(entry["output"])
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
clf = LogisticRegression()
clf.fit(X_vec, y)
save(clf, "model.pkl")
save(vectorizer, "vectorizer.pkl")
print("Model-2 and vectorizer-2 is trained and saved successfully")
