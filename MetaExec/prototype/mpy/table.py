from enum import Enum

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
        __order__ = "qurlyOpen qurlyClose squareOpen squreClose roundOpen roundClose trinagleOpen trinagleClose commentOpen commentClose"
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
        


    
       

