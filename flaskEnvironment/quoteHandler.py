from ai_quotes import ai_quotes 
import random

def randomQuote():
    return random.choice(ai_quotes)

def selectQuote(id):
    for quote in ai_quotes:
        if(quote["id"] == id):
            return quote
    return "Quote not found"
