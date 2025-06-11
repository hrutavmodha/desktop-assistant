from joblib import load
clf = load("model.pkl")
vectorizer = load("vectorizer.pkl")
def get_model_route(query: str) -> str:
    query_vec = vectorizer.transform([query.lower()])
    return clf.predict(query_vec)[0]
if __name__ == "__main__":
    user_query = input("You: ")
    selected_model = get_model_route(user_query)
    print(f"Route this query to: {selected_model}")
