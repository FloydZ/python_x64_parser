# Generated from x64.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .x64Parser import x64Parser
else:
    from x64Parser import x64Parser

# This class defines a complete generic visitor for a parse tree produced by x64Parser.

class x64Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by x64Parser#prog.
    def visitProg(self, ctx:x64Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#line.
    def visitLine(self, ctx:x64Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#instruction.
    def visitInstruction(self, ctx:x64Parser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#lbl.
    def visitLbl(self, ctx:x64Parser.LblContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#extern.
    def visitExtern(self, ctx:x64Parser.ExternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#section.
    def visitSection(self, ctx:x64Parser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#global.
    def visitGlobal(self, ctx:x64Parser.GlobalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#assemblerdirective.
    def visitAssemblerdirective(self, ctx:x64Parser.AssemblerdirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#rw.
    def visitRw(self, ctx:x64Parser.RwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#rb.
    def visitRb(self, ctx:x64Parser.RbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#rs.
    def visitRs(self, ctx:x64Parser.RsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#cseg.
    def visitCseg(self, ctx:x64Parser.CsegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#dseg.
    def visitDseg(self, ctx:x64Parser.DsegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#dw.
    def visitDw(self, ctx:x64Parser.DwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#db.
    def visitDb(self, ctx:x64Parser.DbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#dd.
    def visitDd(self, ctx:x64Parser.DdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#equ.
    def visitEqu(self, ctx:x64Parser.EquContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#if_.
    def visitIf_(self, ctx:x64Parser.If_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#assemblerexpression.
    def visitAssemblerexpression(self, ctx:x64Parser.AssemblerexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#assemblerlogical.
    def visitAssemblerlogical(self, ctx:x64Parser.AssemblerlogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#assemblerterm.
    def visitAssemblerterm(self, ctx:x64Parser.AssemblertermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#endif_.
    def visitEndif_(self, ctx:x64Parser.Endif_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#end.
    def visitEnd(self, ctx:x64Parser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#org.
    def visitOrg(self, ctx:x64Parser.OrgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#title.
    def visitTitle(self, ctx:x64Parser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#include_.
    def visitInclude_(self, ctx:x64Parser.Include_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#expressionlist.
    def visitExpressionlist(self, ctx:x64Parser.ExpressionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#label.
    def visitLabel(self, ctx:x64Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#expression.
    def visitExpression(self, ctx:x64Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx:x64Parser.MultiplyingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#argument.
    def visitArgument(self, ctx:x64Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#ptr.
    def visitPtr(self, ctx:x64Parser.PtrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#dollar.
    def visitDollar(self, ctx:x64Parser.DollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#register_.
    def visitRegister_(self, ctx:x64Parser.Register_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#string_.
    def visitString_(self, ctx:x64Parser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#name.
    def visitName(self, ctx:x64Parser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#number.
    def visitNumber(self, ctx:x64Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#rep.
    def visitRep(self, ctx:x64Parser.RepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#sign.
    def visitSign(self, ctx:x64Parser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by x64Parser#opcode.
    def visitOpcode(self, ctx:x64Parser.OpcodeContext):
        return self.visitChildren(ctx)



del x64Parser