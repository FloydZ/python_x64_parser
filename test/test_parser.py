#! /usr/bin/python3
from antlr4 import *
from antlr4.tree import Trees
from parser.x64Lexer import x64Lexer as ASMLexer
from parser.x64Parser import x64Parser as ASMParser

from parser.parser import *
import sys


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ASMLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ASMParser(stream)
    tree = parser.prog()
    
    visitor = Visitor(tree, parser)
    visitor.visit(tree)
    print(visitor.instructions_list)
    print(visitor.constraints_list)


if __name__ == '__main__':
    main(sys.argv)
