from json import load
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump as save
with open("data.json") as file:
    data = load(file)
pssample = {
    "<query>": ["dogs", "AI", "news", "time machine", "game"],
    "<duration>": ["10 seconds", "2 minutes", "30 seconds", "5 mins", "1 hour"]
}
X, y = [], []
for entry in data:
    intent = entry["output"]
    for template in entry["input"]:
        for placeholder, samples in pssample.items():
            if placeholder in template:
                for sample in samples:
                    X.append(template.replace(placeholder, sample))
                    y.append(intent)
                break
        else:
            X.append(template)
            y.append(intent)
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
clf = LogisticRegression()
clf.fit(X_vec, y)
save(clf, "model.pkl")
save(vectorizer, "vectorizer.pkl")
print("Model-2 and vectorizer-2 is trained and saved successfully")
