#def getModel(query):
from joblib import load
clf = load("backend/model/model4/model4.pkl")
vectorizer = load("backend/model/model4/vectorizer4.pkl")
query = sys.argv[1]
query_vec = vectorizer.transform([query.lower()])
model = clf.predict(query_vec)[0]
print(model)
