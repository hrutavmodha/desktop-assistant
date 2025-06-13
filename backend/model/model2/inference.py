def execDynamicCMD(cmd):
  import nltk
  from nltk import word_tokenize, pos_tag
  from joblib import load
  import sys
  from handlers import googleSearch, wikiSearch
  nltk.download("punkt")
  nltk.download("averaged_perceptron_tagger")
  clf = load("backend/model/model2/model2.pkl")
  vectorizer = load("backend/model/model2/vectorizer2.pkl")
  cmd_vec = vectorizer.transform([cmd])
  intent = clf.predict(cmd_vec)[0]
  term = ""
  tokens = word_tokenize(cmd)
  tagged = pos_tag(tokens) 
  for word, tag in tagged:
      if tag == "NNP":
          term = term + " " + word
  if intent == "search":
      googleSearch(term)
  elif intent == "wiki":
      wikiSearch(term)
  else:
      print("Sorry, I can't find any relevant information")
