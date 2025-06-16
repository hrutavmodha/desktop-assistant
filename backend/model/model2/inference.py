def execDynamicCMD(cmd):
  import nltk
  from nltk import word_tokenize, pos_tag
  from joblib import load
  from handlers import googleSearch, wikiSearch, setTimer
  import os, sys
  nltk.download("punkt")
  nltk.download("averaged_perceptron_tagger")
  basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
  modelFolder = os.path.join(basePath, "backend", "model", "model4")    
  modelPath = os.path.join(modelFolder, "model4.pkl")
  vectorizerPath = os.path.join(modelFolder, "vectorizer4.pkl")
  model = load(modelPath)
  vectorizer = load(vectorizerPath)
  cmd_vec = vectorizer.transform([cmd])
  intent = model.predict(cmd_vec)[0]
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
  elif intent == "timer":
      setTimer(cmd)
  else:
      print("Sorry, I can't find any relevant information or perform any action on your given command. Try be more specific")