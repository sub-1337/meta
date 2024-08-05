from enum import Enum
def retCommonName(nameObj, isEscape):
    return token(nameObj, isEscape)
def retEnumSpace():
    return keywords.common.value.space
def isSapceEnum(obj):
    return obj == keywords.common.value.space
def isSpaceStr(str):
    return  str == keywords.common.value.space.value  
def isBracketStr(str):
    for el in keywords.brackets.value:
        if (el.value == str):
            return True
    return False
def isQuotes(token):
    if (isinstance(token, str)):
        if (token == keywords.brackets.value.quotes.value):
            return True
        else:
            return False
    return token.key == keywords.brackets.value.quotes or \
    token.rawSymbol == keywords.brackets.value.quotes.value
def retEnumQuotes():
    return keywords.brackets.value.quotes
def retEnumBracket(str):
    for elem in keywords.brackets.value:
        if elem.value == str:
            return elem
    return None

def retTokenAuto(token):
    ret = None
    if isSpaceStr(token.rawSymbol):
        ret = retEnumSpace()
    elif isBracketStr(token.rawSymbol):
        ret = retEnumBracket(token.rawSymbol)
    elif isQuotes(token.rawSymbol):
        ret = retEnumQuotes()
    else:
        ret = token.rawSymbol
    return retCommonToken(ret)
def retCommonToken(nameObj, isEscape = False):
    return token(nameObj, isEscape)
def retEnumSpace():
    return keywords.common.value.space
def isSapceEnum(obj):
    return obj == keywords.common.value.space
def isSpaceStr(str):
    return  str == keywords.common.value.space.value  
def isBracketStr(str):
    for el in keywords.brackets.value:
        if (el.value == str):
            return True
    return False
def retEnumBracket(str):
    for elem in keywords.brackets.value:
        if elem.value == str:
            return elem
    return None

class token:    
    rawSymbol = ""
    key = None
    isEscape = False
    def __init__(self, rawSymbol, isEscape = None) -> None:
        if isinstance(rawSymbol, str):
            self.rawSymbol = rawSymbol
        elif isinstance(rawSymbol, Enum):
            self.key = rawSymbol
        elif isinstance(rawSymbol, token):
            self.key = rawSymbol.key
            self.rawSymbol = rawSymbol.rawSymbol
            if isEscape == None:
                self.isEscape =  rawSymbol.isEscape
                return
        self.isEscape = isEscape
    def retStr(self):
        if self.key != None:
            return self.key.value
        elif self.rawSymbol != "":
            return self.rawSymbol
        else:
            return None
    def __repr__(self) -> str:
        rawSymbol = ""
        if self.key != None:
            rawSymbol += str(self.key)
        else:
            rawSymbol += str(self.rawSymbol)
        return "rawSymbol \'" + rawSymbol + "\' esc \'" + str(self.isEscape) + "\'"


class keywords(Enum):    
    class common(Enum):
        none = None
        name = ""
        space = " "
        var = "var"        
        function = "fn"
        new = "new"
        auto = "auto"
        comment = "//"
        const = "const"
        semicolon = ";"
        dollar = "$"
        pointer = "ptr"
        _import = "import"
    class brackets(Enum):
        __order__ = "quotes qurlyOpen qurlyClose squareOpen squreClose roundOpen roundClose trinagleOpen trinagleClose commentOpen commentClose"
        quotes = "\""
        qurlyOpen = "{"
        qurlyClose = "}"
        squareOpen = "["
        squreClose = "]"        
        roundOpen = "("
        roundClose = ")"
        trinagleOpen = "<"
        trinagleClose = ">"
        commentOpen = "/*"
        commentClose = "*/"
    class compare(Enum):
        equal = "=="
        notEqual = "!="
        greater = ">"
        lower = "<"
        greaterOrEq = ">="
        lowerOrEq = "<="
    # example table.keywords.math_keywords.value.mod
    class math_keywords(Enum):
        plus = "+"
        minus = "-"
        mult = "*"
        div = "/"
        mod = "%"
    class embeded_types(Enum):
        char = "char"
        string = "string"
        int = "int"
        real = "real"
        


    
       

