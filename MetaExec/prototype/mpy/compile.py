import table
from table import isSapceEnum, isSpaceStr, isBracket


class Parser():
    tokenMap = None
    maxTokenSz = 6
    tokenized = []
    prep_tokenized = []
    def getReady(self):
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
        self.tokenMap = tokens

    def parse(self, text):  
        textLines = text.splitlines()
        self.tokenized = []
        self.prep_tokenized.clear()
        for line in textLines:
            for i, symbol in enumerate(line):
                if isSpaceStr(symbol):
                    if len(self.prep_tokenized) != 0:
                        if isSapceEnum(self.prep_tokenized[-1]):
                           self.prep_tokenized.append(table.keywords.common.value.space)
                    else:
                        self.prep_tokenized.append(table.keywords.common.value.space)
                elif isBracket(symbol):
                    print(symbol)

def test():
    parser = Parser()
    parser.getReady()
    import os.path as path
    file = open(path.join( "testSrc", "hello.m"))
    parser.parse(file.read())
    print()
if __name__ == "__main__":
    test()

                