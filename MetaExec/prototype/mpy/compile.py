import table

class Parser():
    tokenMap = None
    maxTokenSz = 6
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
                print(keyword.name)
        self.tokenMap = tokens

    def parse(self, text):        
        textLines = text.splitlines()
        tokenized = []
        for line in textLines:
            symCount = 0
            tmpString = ""
            for symbol in line:
                tmpString += symbol
                symCount += 1                
                if symCount > self.maxTokenSz:

                if tmpString in self.tokenMap:
                    tokenized.append(self.tokenMap[tmpString])
                if symbol == " ":
                    tokenized.append(self.tokenMap["name"])
                    tmpString = ""
                    symCount = 0