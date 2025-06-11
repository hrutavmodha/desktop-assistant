import wikipedia
def wikiSearch(query):
    try:
        summary = wikipedia.summary(query, sentences = 2)
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"I am confused. It has several meanings like {e[:5]}. Please specify")
    except wikipedia.exceptions.PageError:
        print("Can't find any information related to your query. Did you meant something else")
    except Exception as e:
        print("An error occured\n{e}")
