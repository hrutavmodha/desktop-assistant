import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
X = y = []
with open("data.json", "r") as file:
    data = json.load(file)
    for entry in data:
        output_command = entry["output"]["windows"]  # change for other OS
        for variant in entry["input"]:
            X.append(variant)
            y.append(output_command)
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)
print("Your Voice Assistant is ready")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting...")
        break
    user_vec = vectorizer.transform([user_input])
    predicted_command = model.predict(user_vec)[0]
    print(f"Bot: {predicted_command}")
