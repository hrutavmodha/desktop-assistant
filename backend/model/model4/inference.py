def getModel(query):
    from joblib import load
    # basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
    # modelFolder = os.path.join(basePath, "backend", "model", "model4")
    # modelPath = os.path.join(modelFolder, "model4.pkl") 
    # vectorizerPath = os.path.join(modelFolder, "vectorizer4.pkl")
    # In production, while building the executable, the model and vectorizer PKL files are taken from PyInstaller's _MEIPASS directory
    # In development, they are taken from the current directory
    # Uncomment the first 4 lines of comment when running in production
    model = load("backend/model/model4/model4.pkl")
    vectorizer = load("backend/model/model4/vectorizer4.pkl")
    query_vec = vectorizer.transform([query.lower()])
    return model.predict(query_vec)[0]
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        query = sys.argv[1]
        result = getModel(query)
        print(result)
    else:
        print("Please provide a query as a command line argument.")