from ai_quotes import ai_quotes 
from unit_tests import *
import random

def randomQuote():
    i = 1
    return random.choice(ai_quotes), 200

def selectQuote(id):
    j = 1
    for quote in ai_quotes:
        if(quote["id"] == id):
            return quote, 200
    return "Quote not found", 404
