#!/usr/bin/python3
""" some tests """
import sys
from antlr4 import *
from antlr4.tree import Trees
from python_x64_parser.nasm.nasm_x86_64_Lexer import nasm_x86_64_Lexer
from python_x64_parser.nasm.nasm_x86_64_Parser import nasm_x86_64_Parser
from python_x64_parser.nasm.nasm_x86_64_ParserVisitor import nasm_x86_64_ParserVisitor


class Visitor(nasm_x86_64_ParserVisitor):
    def __init__(self):
        self.instructionsList = []

    # Visit a parse tree produced by nasm_x86_64_Parser#line.
    def visitInstruction(self, ctx: nasm_x86_64_Parser.InstructionContext):
        self.instructionsList.append(ctx)
        return self.visitChildren(ctx)


def test_simple():
    file = "nasm/addr64x.asm"
    input_stream = FileStream(file)
    lexer = nasm_x86_64_Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = nasm_x86_64_Parser(stream)
    tree = parser.program()

    visitor = Visitor()
    visitor.visitProgram(tree)
    assert len(visitor.instructionsList)
