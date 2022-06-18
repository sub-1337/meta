from ast import Str


inp = """
use console;
main()
{
    print("hello world!");
}
"""

class CodeBit():
    def __init__(self, str):
        self.bit = str

class Code:
    code_bits = None
    def __init__(self, code):
        if type(code) is Code:
            self.bits = code.bits
        elif type(code) is str:
            self.parse(code)
    def parse(self, code):
        parsed = code.split("\n")
        self.code_bits = [CodeBit(bit) for bit in parsed]
        
class Parser:
    code = None
    def __init__(self, code):
        self.parse(code)
    def parse(self,code):
        self.code = Code(code)

parser = Parser(inp)
pass