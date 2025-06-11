from joblib import load
import sys
clf = load("model.pkl")
vectorizer = load("vectorizer.pkl")
cmd = input("You: ").lower()
cmd_vec = vectorizer.transform([cmd])
intent = clf.predict(cmd_vec)[0]
print(f"Predicted intent: {intent}")
