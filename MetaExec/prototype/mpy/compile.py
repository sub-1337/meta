import table
from table import retCommonName, isSapceEnum, isSpaceStr, isBracketStr, retEnumBracket, isQuotes, retEnumQuotes, retEnumSpace


class Parser():
    tokenized = []
    origText = ""
    errorList = []
    def Parse(self, text):
        self.origText = text
        self.parse_basic()
        self.parse_norm_spaces()
    # Roughly parse
    def parse_basic(self):
        textLines = self.origText.splitlines()
        self.tokenized = []
        self.tokenized.clear()
        quotes = False
        for line in textLines:
            for i, symbol in enumerate(line):              
                    
                if isSpaceStr(symbol):
                    self.tokenized.append(retEnumSpace())
                elif isBracketStr(symbol):
                    if isQuotes(symbol):
                        quotes =  not quotes
                        self.tokenized.append(retEnumQuotes())
                    else:
                        self.tokenized.append(retEnumBracket(symbol))
                else:
                    self.tokenized.append(retCommonName(symbol, quotes))
        print("---parse_basic---")
        print(self.tokenized)
    # Delete excessive white spaces
    def parse_norm_spaces(self):
        prev = table.keywords.common.value.none
        prevTokens = self.tokenized
        newTokens = []
        for token in prevTokens:
            if prev == token and isSapceEnum(token):
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

                