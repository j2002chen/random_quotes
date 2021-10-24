from ai_quotes import ai_quotes 
import random

def randomQuote():
    return random.choice(ai_quotes), 200

def selectQuote(id):
    for quote in ai_quotes:
        if(quote["id"] == id):
            return quote, 200
    return "Quote not found", 404
