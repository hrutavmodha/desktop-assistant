def getModel(query):
    from joblib import load
    import sys, os
    basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
    modelFolder = os.path.join(basePath, "backend", "model", "model4")
    modelPath = os.path.join(modelFolder, "model4.pkl") 
    vectorizerPath = os.path.join(modelFolder, "vectorizer4.pkl")
    model = load(modelPath)
    vectorizer = load(vectorizerPath)
    query_vec = vectorizer.transform([query.lower()])
    return model.predict(query_vec)[0]