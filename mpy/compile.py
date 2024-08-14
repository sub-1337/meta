from table import isEscape, isSpace, retTokenAuto, retCommonToken, isQuotes, isTab, retSpace

class Parser():
    tokenized = []
    origText = ""
    errorList = []
    def Parse(self, text):
        self.origText = text
        self.parse_basic()
        self.parse_one_symbols()
        self.parse_quotes()
        self.parse_swap_tabs()
        self.parse_norm_spaces()
    # Create basic tokens
    def parse_basic(self):
        textLines = self.origText.splitlines()
        self.tokenized = []
        self.tokenized.clear()
        newTokens = []
        for line in textLines:
            for i, symbol in enumerate(line):          
                newTokens.append(retCommonToken(symbol, False))
        self.tokenized = newTokens
    # parse single symbol if possible
    def parse_one_symbols(self):
        prevTokens = self.tokenized
        newTokens = []
        self.tokenized = newTokens
        for i, symbol in enumerate(prevTokens):
            newTokens.append(retTokenAuto(symbol))
        self.tokenized = newTokens
    # Set quotes
    def parse_quotes(self):        
        quotes = False
        prevTokens = self.tokenized
        newTokens = []
        for i, token in enumerate(prevTokens):                     
            newTokens.append(retCommonToken(token, quotes))
            if isQuotes(token):
                quotes =  not quotes   
        prevTokens = newTokens
        newTokens = []
        # Algorythm to escape only inner string of " "
        for i, token in enumerate(prevTokens): 
            if isQuotes(token):
                quotes =  not quotes   
            resQutes = token.isEscape
            newTokens.append(retCommonToken(token, quotes and resQutes))            
        self.tokenized = newTokens
    # Swap tabs with spaces
    def parse_swap_tabs(self):
        prevTokens = self.tokenized
        newTokens = []
        for token in prevTokens:
            if isTab(token):
                if not isEscape(token):
                    newTokens.append(retSpace())
                else:
                    newTokens.append(token)
            else:
                newTokens.append(token)
        self.tokenized = newTokens
    # Delete excessive white spaces
    def parse_norm_spaces(self):
        prevSpace = False
        prevTokens = self.tokenized
        newTokens = []
        for token in prevTokens:
            if isSpace(token) and not isEscape(token):
                if not prevSpace:
                    newTokens.append(token)
                prevSpace = True
            else:
                prevSpace = False
                newTokens.append(token)
        self.tokenized = newTokens
    def parse_delete_comments(self):
        prevTokens = self.tokenized
        newTokens = []
        for token in prevTokens:
            

def test():
    parser = Parser()
    import os.path as path
    file = open(path.join( "testSrc", "hello.m"))
    parser.Parse(file.read())
    print(parser.tokenized)
if __name__ == "__main__":
    test()

                