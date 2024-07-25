import table

class Parser():
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
        #print(tokens)

    def parse(self, text):
        textLines = text.splitlines()
        for symbol 
        pass