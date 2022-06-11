inp = """
use console;
main()
{
    print("hello world!");
}
"""

class Code:
    def __init__(self, code : str):
        parsed = code.split("\n")
        
class Parser:
    code = None
    def parse(self,code):
        if code is Code:
            self.code = Code(code)
        elif code is str:
            self.code = Code()
