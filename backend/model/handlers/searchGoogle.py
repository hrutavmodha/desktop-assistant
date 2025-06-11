import webbrowser as web
from urllib.parse import quote_plus as encodeurl
def googleSearch(query):
    search = encodeurl(uquery)
    web.open(f"https://www.google.com/search?q={search}")
