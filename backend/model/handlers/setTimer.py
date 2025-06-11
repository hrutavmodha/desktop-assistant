import nltk
import threading
import time
from nltk.tokenize import word_tokenize
def extractDuration(text):
    tokens = word_tokenize(text.lower())
    value = None
    unit = None
    for i, token in enumerate(tokens):
        if token.isdigit():
            value = int(token)
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                if next_token in ["second", "seconds", "minute", "minutes"]:
                    unit = next_token
                    break
    if value and unit:
        return value * 60 if "minute" in unit else value
    return None
def setTimer(cmd, speak):
    duration = extractDuration(cmd)
    if not duration:
        print("Sorry, couldn't detect a valid timer duration.")
        return
    print(f"Setting timer for {duration // 60} minutes" if duration >= 60 else f"Setting timer for {duration} seconds")
    def countdown():
        time.sleep(duration)
        print("Time's up!")
    threading.Thread(target = countdown).start()
