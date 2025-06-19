def execDynamicCMD(cmd):
#   import nltk
  from nltk import word_tokenize, pos_tag
  from joblib import load
  from backend.model.model2.handlers.googleSearch import googleSearch
  from backend.model.model2.handlers.wikiSearch import wikiSearch
#   nltk.download("punkt")
#   nltk.download("averaged_perceptron_tagger")
#   basePath = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
#   modelFolder = os.path.join(basePath, "backend", "model", "model2")    
#   modelPath = os.path.join(modelFolder, "model2.pkl")
#   vectorizerPath = os.path.join(modelFolder, "vectorizer2.pkl")
  model = load("backend/model/model2/model2.pkl")
  vectorizer = load("backend/model/model2/vectorizer2.pkl")
  cmd_vec = vectorizer.transform([cmd])
  intent = model.predict(cmd_vec)[0]
  term = ""
  res = ""
  tokens = word_tokenize(cmd)
  tagged = pos_tag(tokens) 
  for word, tag in tagged:
      if tag == "NNP":
          term = term + " " + word
  if intent == "search":
      googleSearch(term)
  elif intent == "wiki":
      res = wikiSearch(cmd)
  else:
      res = "I'm Sorry, I can't find any relevant information or perform any action on your given command. Try be more specific"
  return res