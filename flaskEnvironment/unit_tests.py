from app import *
import quoteHandler
from ai_quotes import ai_quotes
global i,j,k
i,j,k = 0

class TestClass:

    def randomQuoteTest():
        assert ai_quotes.contains(randomQuote())
        
    def selectQuoteTest():
        for id in range(0,9):
            success = false
            for quote in ai_quotes:
                if(quote["id"] == id):
                    success = true
            assert success == true

    def regularCaseTest():
        val = ai_quotes.ID
        assert Quote.get(self,val) == quoteHandler.randomChoice()

    def errorCaseTest(): 
        #idk val = 
        assert Quote.get(self,val) == quoteHandler.error404()
