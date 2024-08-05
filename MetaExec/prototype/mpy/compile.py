import table
from table import retTokenAuto, retCommonToken, isSapceEnum, isSpaceStr, isBracketStr, retEnumBracket, isQuotes, retEnumQuotes, retEnumSpace


class Parser():
    tokenized = []
    origText = ""
    errorList = []
    def Parse(self, text):
        self.origText = text
        self.parse_basic()
        self.parse_one_symbols()
        self.parse_quotes()
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
        print("---parse_basic---")
        print(self.tokenized)
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
        for i, symbol in enumerate(prevTokens):
            if isQuotes(symbol):
                quotes =  not quotes
            newTokens.append(retCommonToken(symbol, quotes))
        self.tokenized = newTokens

    # Delete excessive white spaces
    def parse_norm_spaces(self):
        prev = table.keywords.common.value.none
        prevTokens = self.tokenized
        newTokens = []
        for token in prevTokens:
            if prev == token.key and isSapceEnum(token):
                next
            else:
                newTokens.append(token)
            prev = token
        self.tokenized = newTokens
        print("---parse_norm---")
        print(self.tokenized)

            

def test():
    parser = Parser()
    import os.path as path
    file = open(path.join( "testSrc", "hello.m"))
    parser.Parse(file.read())
    print()
if __name__ == "__main__":
    test()

                