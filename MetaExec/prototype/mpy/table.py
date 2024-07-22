from enum import Enum




class keywords(Enum):
    var = "var"
    function = "fn"
    new = "new"
    auto = "auto"
    comment = "//"
    const = "const"
    semicolon = ";"
    dollar = "$"
    pointer = "ptr"
    class brackets(Enum):
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
        


    
       

