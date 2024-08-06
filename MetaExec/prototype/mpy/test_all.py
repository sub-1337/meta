import compile
parser = compile.Parser()
import os.path as path
file = open(path.join( "testSrc", "hello.m"))
parser.Parse(file.read())
print(parser.tokenized)