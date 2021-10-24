from app import *
from quoteHandler import *
from ai_quotes import ai_quotes

class TestClass:

    def test_randomQuotes():
        assert ai_quotes.contains(randomQuote())
        
    def test_selectQuote():
        for id in range(0,9):
            success = False
            for quote in ai_quotes:
                if(quote["id"] == id):
                    success = True
            assert success == True

