Installation
============

Automatic:
----------
```bash
pip install https://github.com/FloydZ/python_x64_parser
```

Manual:
------
```
git clone --recursive https://github.com/FloydZ/python_x64_parser
cd python_x64_parser/nasm
make
```

The `make` command generates the needed python files from the antlr model.

Usage:
======
Example for the `nasm` syntax:
```python3
from antlr4 import *
from python_x64_parser.nasm.nasm_x86_64_Lexer import nasm_x86_64_Lexer
from python_x64_parser.nasm.nasm_x86_64_Parser import nasm_x86_64_Parser
from python_x64_parser.nasm.nasm_x86_64_ParserVisitor import nasm_x86_64_ParserVisitor

class Visitor(nasm_x86_64_ParserVisitor):
    """Example Parser for listing all instructions"""
    def __init__(self):
        self.instructionsList = []

    def visitInstruction(self, ctx: nasm_x86_64_Parser.InstructionContext):
        self.instructionsList.append(ctx)
        return self.visitChildren(ctx)


file = "nasm/addr64x.asm"
input_stream = FileStream(file)
lexer = nasm_x86_64_Lexer(input_stream)
stream = CommonTokenStream(lexer)
parser = nasm_x86_64_Parser(stream)
tree = parser.program()

visitor = Visitor()
visitor.visitProgram(tree)
```

for more examples look at the [test folder](https://github.com/FloydZ/python_x64_parser/tree/master/test)