from joblib import load
from handlers.searchGoogle import searchGoogle
from handlers.wikiSearch import wikiSearch
from handlers.setTimer import setTimer
model = load("model.pkl")
while True:
    user_input = sys.argv[1]
    browse = re.search(r"(?:search|look\s*up|google)\s+(.*)", user_input, flags = re.I)
    wiki = re.search(r"(?:what is|who is|define|tell me about|give info about)\s+(.*)", cmd, re.I)
    if user_input.lower() in ["exit", "quit", "bye", "go off", "goodbye"]:
        print("Bye")
        break
    elif browse:
        query = browse.group(1)
        searchGoogle(query)
    elif wiki:
        query = wiki.group(1)
        wikiSearch(query)
else:
    user_vec = vectorizer.transform([user_input])
    predicted_command = model.predict(user_vec)[0]
    print("Understood your command. Processing it, it may take few moment. Please wait")
    os.system(predicted_command)
