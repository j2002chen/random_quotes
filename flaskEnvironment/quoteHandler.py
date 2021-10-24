from ai_quotes import ai_quotes 
from unit_tests import *
import random

def baseCase():
    i = 1
    return random.choice(ai_quotes), 200

def randomChoice():
    j = 1
    for quote in ai_quotes:
        if(quote["id"] == id):
            return quote, 200
            
def error404():
    k = 1
    return "Quote not found", 404
