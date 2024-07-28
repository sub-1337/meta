import table

t = table.keywords.common.value.const
t2 = table.keywords.math_keywords.value.mod

assert table.isQuotes("\"")

import compile
parser = compile.Parser()
parser.getReady()
import os.path as path
file = open(path.join( "testSrc", "hello.m"))
parser.parse(file.read())
print()