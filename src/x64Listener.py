# Generated from x64.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .x64Parser import x64Parser
else:
    from x64Parser import x64Parser

# This class defines a complete listener for a parse tree produced by x64Parser.
class x64Listener(ParseTreeListener):

    # Enter a parse tree produced by x64Parser#prog.
    def enterProg(self, ctx:x64Parser.ProgContext):
        pass

    # Exit a parse tree produced by x64Parser#prog.
    def exitProg(self, ctx:x64Parser.ProgContext):
        pass


    # Enter a parse tree produced by x64Parser#line.
    def enterLine(self, ctx:x64Parser.LineContext):
        pass

    # Exit a parse tree produced by x64Parser#line.
    def exitLine(self, ctx:x64Parser.LineContext):
        pass


    # Enter a parse tree produced by x64Parser#instruction.
    def enterInstruction(self, ctx:x64Parser.InstructionContext):
        pass

    # Exit a parse tree produced by x64Parser#instruction.
    def exitInstruction(self, ctx:x64Parser.InstructionContext):
        pass


    # Enter a parse tree produced by x64Parser#lbl.
    def enterLbl(self, ctx:x64Parser.LblContext):
        pass

    # Exit a parse tree produced by x64Parser#lbl.
    def exitLbl(self, ctx:x64Parser.LblContext):
        pass


    # Enter a parse tree produced by x64Parser#extern.
    def enterExtern(self, ctx:x64Parser.ExternContext):
        pass

    # Exit a parse tree produced by x64Parser#extern.
    def exitExtern(self, ctx:x64Parser.ExternContext):
        pass


    # Enter a parse tree produced by x64Parser#section.
    def enterSection(self, ctx:x64Parser.SectionContext):
        pass

    # Exit a parse tree produced by x64Parser#section.
    def exitSection(self, ctx:x64Parser.SectionContext):
        pass


    # Enter a parse tree produced by x64Parser#global.
    def enterGlobal(self, ctx:x64Parser.GlobalContext):
        pass

    # Exit a parse tree produced by x64Parser#global.
    def exitGlobal(self, ctx:x64Parser.GlobalContext):
        pass


    # Enter a parse tree produced by x64Parser#assemblerdirective.
    def enterAssemblerdirective(self, ctx:x64Parser.AssemblerdirectiveContext):
        pass

    # Exit a parse tree produced by x64Parser#assemblerdirective.
    def exitAssemblerdirective(self, ctx:x64Parser.AssemblerdirectiveContext):
        pass


    # Enter a parse tree produced by x64Parser#rw.
    def enterRw(self, ctx:x64Parser.RwContext):
        pass

    # Exit a parse tree produced by x64Parser#rw.
    def exitRw(self, ctx:x64Parser.RwContext):
        pass


    # Enter a parse tree produced by x64Parser#rb.
    def enterRb(self, ctx:x64Parser.RbContext):
        pass

    # Exit a parse tree produced by x64Parser#rb.
    def exitRb(self, ctx:x64Parser.RbContext):
        pass


    # Enter a parse tree produced by x64Parser#rs.
    def enterRs(self, ctx:x64Parser.RsContext):
        pass

    # Exit a parse tree produced by x64Parser#rs.
    def exitRs(self, ctx:x64Parser.RsContext):
        pass


    # Enter a parse tree produced by x64Parser#cseg.
    def enterCseg(self, ctx:x64Parser.CsegContext):
        pass

    # Exit a parse tree produced by x64Parser#cseg.
    def exitCseg(self, ctx:x64Parser.CsegContext):
        pass


    # Enter a parse tree produced by x64Parser#dseg.
    def enterDseg(self, ctx:x64Parser.DsegContext):
        pass

    # Exit a parse tree produced by x64Parser#dseg.
    def exitDseg(self, ctx:x64Parser.DsegContext):
        pass


    # Enter a parse tree produced by x64Parser#dw.
    def enterDw(self, ctx:x64Parser.DwContext):
        pass

    # Exit a parse tree produced by x64Parser#dw.
    def exitDw(self, ctx:x64Parser.DwContext):
        pass


    # Enter a parse tree produced by x64Parser#db.
    def enterDb(self, ctx:x64Parser.DbContext):
        pass

    # Exit a parse tree produced by x64Parser#db.
    def exitDb(self, ctx:x64Parser.DbContext):
        pass


    # Enter a parse tree produced by x64Parser#dd.
    def enterDd(self, ctx:x64Parser.DdContext):
        pass

    # Exit a parse tree produced by x64Parser#dd.
    def exitDd(self, ctx:x64Parser.DdContext):
        pass


    # Enter a parse tree produced by x64Parser#equ.
    def enterEqu(self, ctx:x64Parser.EquContext):
        pass

    # Exit a parse tree produced by x64Parser#equ.
    def exitEqu(self, ctx:x64Parser.EquContext):
        pass


    # Enter a parse tree produced by x64Parser#if_.
    def enterIf_(self, ctx:x64Parser.If_Context):
        pass

    # Exit a parse tree produced by x64Parser#if_.
    def exitIf_(self, ctx:x64Parser.If_Context):
        pass


    # Enter a parse tree produced by x64Parser#assemblerexpression.
    def enterAssemblerexpression(self, ctx:x64Parser.AssemblerexpressionContext):
        pass

    # Exit a parse tree produced by x64Parser#assemblerexpression.
    def exitAssemblerexpression(self, ctx:x64Parser.AssemblerexpressionContext):
        pass


    # Enter a parse tree produced by x64Parser#assemblerlogical.
    def enterAssemblerlogical(self, ctx:x64Parser.AssemblerlogicalContext):
        pass

    # Exit a parse tree produced by x64Parser#assemblerlogical.
    def exitAssemblerlogical(self, ctx:x64Parser.AssemblerlogicalContext):
        pass


    # Enter a parse tree produced by x64Parser#assemblerterm.
    def enterAssemblerterm(self, ctx:x64Parser.AssemblertermContext):
        pass

    # Exit a parse tree produced by x64Parser#assemblerterm.
    def exitAssemblerterm(self, ctx:x64Parser.AssemblertermContext):
        pass


    # Enter a parse tree produced by x64Parser#endif_.
    def enterEndif_(self, ctx:x64Parser.Endif_Context):
        pass

    # Exit a parse tree produced by x64Parser#endif_.
    def exitEndif_(self, ctx:x64Parser.Endif_Context):
        pass


    # Enter a parse tree produced by x64Parser#end.
    def enterEnd(self, ctx:x64Parser.EndContext):
        pass

    # Exit a parse tree produced by x64Parser#end.
    def exitEnd(self, ctx:x64Parser.EndContext):
        pass


    # Enter a parse tree produced by x64Parser#org.
    def enterOrg(self, ctx:x64Parser.OrgContext):
        pass

    # Exit a parse tree produced by x64Parser#org.
    def exitOrg(self, ctx:x64Parser.OrgContext):
        pass


    # Enter a parse tree produced by x64Parser#title.
    def enterTitle(self, ctx:x64Parser.TitleContext):
        pass

    # Exit a parse tree produced by x64Parser#title.
    def exitTitle(self, ctx:x64Parser.TitleContext):
        pass


    # Enter a parse tree produced by x64Parser#include_.
    def enterInclude_(self, ctx:x64Parser.Include_Context):
        pass

    # Exit a parse tree produced by x64Parser#include_.
    def exitInclude_(self, ctx:x64Parser.Include_Context):
        pass


    # Enter a parse tree produced by x64Parser#expressionlist.
    def enterExpressionlist(self, ctx:x64Parser.ExpressionlistContext):
        pass

    # Exit a parse tree produced by x64Parser#expressionlist.
    def exitExpressionlist(self, ctx:x64Parser.ExpressionlistContext):
        pass


    # Enter a parse tree produced by x64Parser#label.
    def enterLabel(self, ctx:x64Parser.LabelContext):
        pass

    # Exit a parse tree produced by x64Parser#label.
    def exitLabel(self, ctx:x64Parser.LabelContext):
        pass


    # Enter a parse tree produced by x64Parser#expression.
    def enterExpression(self, ctx:x64Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by x64Parser#expression.
    def exitExpression(self, ctx:x64Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by x64Parser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:x64Parser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by x64Parser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:x64Parser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by x64Parser#argument.
    def enterArgument(self, ctx:x64Parser.ArgumentContext):
        pass

    # Exit a parse tree produced by x64Parser#argument.
    def exitArgument(self, ctx:x64Parser.ArgumentContext):
        pass


    # Enter a parse tree produced by x64Parser#ptr.
    def enterPtr(self, ctx:x64Parser.PtrContext):
        pass

    # Exit a parse tree produced by x64Parser#ptr.
    def exitPtr(self, ctx:x64Parser.PtrContext):
        pass


    # Enter a parse tree produced by x64Parser#dollar.
    def enterDollar(self, ctx:x64Parser.DollarContext):
        pass

    # Exit a parse tree produced by x64Parser#dollar.
    def exitDollar(self, ctx:x64Parser.DollarContext):
        pass


    # Enter a parse tree produced by x64Parser#register_.
    def enterRegister_(self, ctx:x64Parser.Register_Context):
        pass

    # Exit a parse tree produced by x64Parser#register_.
    def exitRegister_(self, ctx:x64Parser.Register_Context):
        pass


    # Enter a parse tree produced by x64Parser#string_.
    def enterString_(self, ctx:x64Parser.String_Context):
        pass

    # Exit a parse tree produced by x64Parser#string_.
    def exitString_(self, ctx:x64Parser.String_Context):
        pass


    # Enter a parse tree produced by x64Parser#name.
    def enterName(self, ctx:x64Parser.NameContext):
        pass

    # Exit a parse tree produced by x64Parser#name.
    def exitName(self, ctx:x64Parser.NameContext):
        pass


    # Enter a parse tree produced by x64Parser#number.
    def enterNumber(self, ctx:x64Parser.NumberContext):
        pass

    # Exit a parse tree produced by x64Parser#number.
    def exitNumber(self, ctx:x64Parser.NumberContext):
        pass


    # Enter a parse tree produced by x64Parser#rep.
    def enterRep(self, ctx:x64Parser.RepContext):
        pass

    # Exit a parse tree produced by x64Parser#rep.
    def exitRep(self, ctx:x64Parser.RepContext):
        pass


    # Enter a parse tree produced by x64Parser#sign.
    def enterSign(self, ctx:x64Parser.SignContext):
        pass

    # Exit a parse tree produced by x64Parser#sign.
    def exitSign(self, ctx:x64Parser.SignContext):
        pass


    # Enter a parse tree produced by x64Parser#opcode.
    def enterOpcode(self, ctx:x64Parser.OpcodeContext):
        pass

    # Exit a parse tree produced by x64Parser#opcode.
    def exitOpcode(self, ctx:x64Parser.OpcodeContext):
        pass



del x64Parser