#def execDynamicCMD(cmd):
from joblib import load
import sys
cmd = sys.argv[1]
clf = load("backend/model/model2/model.pkl")
vectorizer = load("backend/model/model2/vectorizer.pkl")
cmd_vec = vectorizer.transform([cmd])
intent = clf.predict(cmd_vec)[0]
print(f"Predicted intent: {intent}")
