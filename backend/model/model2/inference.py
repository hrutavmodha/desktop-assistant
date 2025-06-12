#def execDynamicCMD(cmd):
from joblib import load
import sys
cmd = sys.argv[1]
clf = load("backend/model/model2/model2.pkl")
vectorizer = load("backend/model/model2/vectorizer2.pkl")
cmd_vec = vectorizer.transform([cmd])
intent = clf.predict(cmd_vec)[0]
print(f"Predicted intent: {intent}")
