def wikiSearch(query):
    import wikipedia as wiki
    try:
        summary = wiki.summary(query, sentences = 2)
        print(summary)
    except wiki.exceptions.DisambiguationError as e:
        print(f"I am confused. It has several meanings like {e[:5]}. Please specify")
    except wiki.exceptions.PageError:
        print("Can't find any information related to your query. Did you meant something else")
    except Exception as e:
        print("An error occured\n{e}")
