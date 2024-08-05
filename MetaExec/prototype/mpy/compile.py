import table
<<<<<<< HEAD
from table import retTokenAuto, retCommonToken, isSapceEnum, isSpaceStr, isBracketStr, retEnumBracket, isQuotes, retEnumQuotes, retEnumSpace
=======
from table import retCommonName, isSapceEnum, isSpaceStr, isBracketStr, retEnumBracket, isQuotes, retEnumQuotes, retEnumSpace
>>>>>>> d4d52f0793ce06010024b8c5bd374c710a06d4d7


class Parser():
    tokenized = []
    origText = ""
    errorList = []
    def Parse(self, text):
        self.origText = text
        self.parse_basic()
<<<<<<< HEAD
        self.parse_one_symbols()
        self.parse_quotes()
        self.parse_norm_spaces()
    # Create tokens
=======
        self.parse_norm_spaces()
    # Roughly parse
>>>>>>> d4d52f0793ce06010024b8c5bd374c710a06d4d7
    def parse_basic(self):
        textLines = self.origText.splitlines()
        self.tokenized = []
        self.tokenized.clear()
<<<<<<< HEAD
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
        for i, symbol in enumerate(self.tokenized):
            if isQuotes(symbol):
                quotes =  not quotes
            newTokens.append(retCommonToken(symbol, quotes))
        self.tokenized = newTokens

=======
        quotes = False
        for line in textLines:
            for i, symbol in enumerate(line):          
                if isSpaceStr(symbol):
                    self.tokenized.append(retEnumSpace())
                elif isBracketStr(symbol):
                    if isQuotes(symbol):
                        quotes =  not quotes
                        self.tokenized.append(retCommonName(retEnumQuotes(), quotes))
                    else:
                        self.tokenized.append(retEnumBracket(symbol))
                else:
                    self.tokenized.append(retCommonName(symbol, quotes))
        print("---parse_basic---")
        print(self.tokenized)
>>>>>>> d4d52f0793ce06010024b8c5bd374c710a06d4d7
    # Delete excessive white spaces
    def parse_norm_spaces(self):
        prev = table.keywords.common.value.none
        prevTokens = self.tokenized
        newTokens = []
        for token in prevTokens:
<<<<<<< HEAD
            if prev == token.key and isSapceEnum(token):
=======
            if prev == token and isSapceEnum(token):
>>>>>>> d4d52f0793ce06010024b8c5bd374c710a06d4d7
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

                