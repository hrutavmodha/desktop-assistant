def getModel(query):
    from joblib import load
    import sys
    clf = load("backend/model/model4/model4.pkl")
    vectorizer = load("backend/model/model4/vectorizer4.pkl")
    query_vec = vectorizer.transform([query.lower()])
    return clf.predict(query_vec)[0]