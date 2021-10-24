from app import *
import quoteHandler
from ai_quotes import ai_quotes
global i,j,k
i,j,k = 0

class TestClass:
    def basecaseTest():
        val = 0
        assert Quote.get(self,val) == quoteHandler.baseCase()

    def regularCaseTest():
        val = ai_quotes.ID
        assert Quote.get(self,val) == quoteHandler.randomChoice()

    def errorCaseTest(): 
        #idk val = 
        assert Quote.get(self,val) == quoteHandler.error404()
