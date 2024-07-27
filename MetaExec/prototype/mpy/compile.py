import table
from table import isSapceEnum, isSpaceStr, isBracket, retEnumBracket


class Parser():
    #tokenMap = None
    #maxTokenSz = 6
    tokenized = []
    origText = ""
    """def getReady(self):
        tokens = {}
        for keywordCathegories in table.keywords:
            for keyword in keywordCathegories.value:
                if not keyword in tokens:
                    tokens[keyword.value] = keyword
                else:
                    if type(tokens[keyword.value]) == type([]):
                         tokens[keyword.value].append(keyword.name)
                    else:
                        oldval = tokens[keyword.value]
                        tokens[keyword.value] = [oldval, keyword.name]
                #print(keyword.name)
        self.tokenMap = tokens"""
    def Parse(self, text):
        self.origText = text
        self.parse_basic()
        self.parse_norm_spaces()
    # Roughly parse
    def parse_basic(self):
        textLines = self.origText.splitlines()
        self.tokenized = []
        self.tokenized.clear()
        for line in textLines:
            for i, symbol in enumerate(line):
                if isSpaceStr(symbol):
                    self.tokenized.append(table.keywords.common.value.space)
                elif isBracket(symbol):
                    self.tokenized.append(retEnumBracket(symbol))
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

                