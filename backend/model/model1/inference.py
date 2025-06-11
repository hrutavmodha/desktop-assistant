from joblib import load
model = load("model.pkl")
vectorizer = load("vectorizer.pkl")
user_input = input("You: ").lower()
user_vec = vectorizer.transform([user_input])
predicted_command = model.predict(user_vec)[0]
print("Understood your command. Processing it, it may take few moment. Please wait")
os.system(predicted_command)
