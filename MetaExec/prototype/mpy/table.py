from enum import Enum
def retCommonName(nameObj, isEscape):
    return name(nameObj, isEscape)
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
def isQuotes(str):
    return str == keywords.brackets.value.quotes.value
def retEnumQuotes():
    return keywords.brackets.value.quotes
def retEnumBracket(str):
    for elem in keywords.brackets.value:
        if elem.value == str:
            return elem
    return None

class name:    
    name = ""
    key = None
    isEscape = False
    def __init__(self, name, isEscape) -> None:
        if type(name) == type(""):
            self.name = name
        elif type(name) == type(Enum):
            key = name
        self.isEscape = isEscape
    def retStr(self):
        if self.key != None:
            return self.key.value
        elif name != "":
            return self.name
    def __repr__(self) -> str:
        name = ""
        if self.key != None:
            name += str(key)
        else:
            name += str(self.name)
        return "Name \'" + name + "\' esc \'" + str(self.isEscape) + "\'"

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
        


    
       

