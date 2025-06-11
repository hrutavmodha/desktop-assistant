def getModel(query):
    from joblib import load
    clf = load("model.pkl")
    vectorizer = load("vectorizer.pkl")
    query_vec = vectorizer.transform([query.lower()])
    return clf.predict(query_vec)[0]
