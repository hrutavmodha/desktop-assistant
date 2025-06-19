def wikiSearch(query):
    import wikipedia as wiki
    try:
        search = wiki.search(query)[0]
        summary = wiki.summary(search, sentences=2)
        if not summary:
            return "No summary available for the search result."
        return summary
    except wiki.exceptions.DisambiguationError as e:
        return  f"I am confused. It has several meanings like {e.options[:5]}. Please specify"
    except wiki.exceptions.PageError:
        return "Can't find any information related to your query. Did you meant something else?"
    except Exception as e:
        return f"An error occured\n{e}"
