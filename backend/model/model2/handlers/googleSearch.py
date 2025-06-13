def googleSearch(query):
    import webbrowser as web
    from urllib.parse import quote_plus as encodeurl
    search = encodeurl(query)
    web.open(f"https://www.google.com/search?q={search}")
