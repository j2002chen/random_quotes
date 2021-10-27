from app import *
from quoteHandler import *
from ai_quotes import ai_quotes

def test_randomQuotes():
    quote = randomQuote()
    assert (quote in ai_quotes) == True
           
def test_selectQuote():
    for id in range(0,9):
        success = False
        for quote in ai_quotes:
            if(quote["id"] == id):
                success = True
        assert success == True

