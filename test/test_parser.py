#! /usr/bin/python3
import sys
from antlr4 import *
from antlr4.tree import Trees
from python_x64_parser.nasm.nasm_x86_64_Lexer import nasm_x86_64_Lexer as ASMLexer
from python_x64_parser.nasm.nasm_x86_64_Parser import nasm_x86_64_Parser as ASMParser


class Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by nasm_x86_64_Parser#program.
    def visitProgram(self, ctx:nasm_x86_64_Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#line.
    def visitLine(self, ctx:nasm_x86_64_Parser.LineContext):
        print(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#label.
    def visitLabel(self, ctx:nasm_x86_64_Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#directive.
    def visitDirective(self, ctx:nasm_x86_64_Parser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#bits.
    def visitBits(self, ctx:nasm_x86_64_Parser.BitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#decimal_integer.
    def visitDecimal_integer(self, ctx:nasm_x86_64_Parser.Decimal_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#use16.
    def visitUse16(self, ctx:nasm_x86_64_Parser.Use16Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#use32.
    def visitUse32(self, ctx:nasm_x86_64_Parser.Use32Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#default.
    def visitDefault(self, ctx:nasm_x86_64_Parser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#default_perfix.
    def visitDefault_perfix(self, ctx:nasm_x86_64_Parser.Default_perfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#section.
    def visitSection(self, ctx:nasm_x86_64_Parser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#section_params.
    def visitSection_params(self, ctx:nasm_x86_64_Parser.Section_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#name.
    def visitName(self, ctx:nasm_x86_64_Parser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#attribute.
    def visitAttribute(self, ctx:nasm_x86_64_Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#section_type.
    def visitSection_type(self, ctx:nasm_x86_64_Parser.Section_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#classs.
    def visitClasss(self, ctx:nasm_x86_64_Parser.ClasssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#overlay.
    def visitOverlay(self, ctx:nasm_x86_64_Parser.OverlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#designation.
    def visitDesignation(self, ctx:nasm_x86_64_Parser.DesignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#allocation.
    def visitAllocation(self, ctx:nasm_x86_64_Parser.AllocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#execution.
    def visitExecution(self, ctx:nasm_x86_64_Parser.ExecutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#writing.
    def visitWriting(self, ctx:nasm_x86_64_Parser.WritingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#starting_possition.
    def visitStarting_possition(self, ctx:nasm_x86_64_Parser.Starting_possitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#follow.
    def visitFollow(self, ctx:nasm_x86_64_Parser.FollowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#flat.
    def visitFlat(self, ctx:nasm_x86_64_Parser.FlatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#absolute_seg.
    def visitAbsolute_seg(self, ctx:nasm_x86_64_Parser.Absolute_segContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#alingment.
    def visitAlingment(self, ctx:nasm_x86_64_Parser.AlingmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#comdat.
    def visitComdat(self, ctx:nasm_x86_64_Parser.ComdatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#tls.
    def visitTls(self, ctx:nasm_x86_64_Parser.TlsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#absolute.
    def visitAbsolute(self, ctx:nasm_x86_64_Parser.AbsoluteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#integer.
    def visitInteger(self, ctx:nasm_x86_64_Parser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#extern.
    def visitExtern(self, ctx:nasm_x86_64_Parser.ExternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#extern_params.
    def visitExtern_params(self, ctx:nasm_x86_64_Parser.Extern_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#wrt.
    def visitWrt(self, ctx:nasm_x86_64_Parser.WrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#weak.
    def visitWeak(self, ctx:nasm_x86_64_Parser.WeakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#required.
    def visitRequired(self, ctx:nasm_x86_64_Parser.RequiredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#globall.
    def visitGloball(self, ctx:nasm_x86_64_Parser.GloballContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#global_params.
    def visitGlobal_params(self, ctx:nasm_x86_64_Parser.Global_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#global_type.
    def visitGlobal_type(self, ctx:nasm_x86_64_Parser.Global_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#visibility.
    def visitVisibility(self, ctx:nasm_x86_64_Parser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#binding.
    def visitBinding(self, ctx:nasm_x86_64_Parser.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#common.
    def visitCommon(self, ctx:nasm_x86_64_Parser.CommonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#common_params.
    def visitCommon_params(self, ctx:nasm_x86_64_Parser.Common_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#near.
    def visitNear(self, ctx:nasm_x86_64_Parser.NearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#far.
    def visitFar(self, ctx:nasm_x86_64_Parser.FarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#static.
    def visitStatic(self, ctx:nasm_x86_64_Parser.StaticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#cpu.
    def visitCpu(self, ctx:nasm_x86_64_Parser.CpuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#float_name.
    def visitFloat_name(self, ctx:nasm_x86_64_Parser.Float_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#float_params.
    def visitFloat_params(self, ctx:nasm_x86_64_Parser.Float_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#warning.
    def visitWarning(self, ctx:nasm_x86_64_Parser.WarningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#warning_state.
    def visitWarning_state(self, ctx:nasm_x86_64_Parser.Warning_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#warning_class.
    def visitWarning_class(self, ctx:nasm_x86_64_Parser.Warning_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#warning_name.
    def visitWarning_name(self, ctx:nasm_x86_64_Parser.Warning_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#push.
    def visitPush(self, ctx:nasm_x86_64_Parser.PushContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#pop.
    def visitPop(self, ctx:nasm_x86_64_Parser.PopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#org.
    def visitOrg(self, ctx:nasm_x86_64_Parser.OrgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#mapp.
    def visitMapp(self, ctx:nasm_x86_64_Parser.MappContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#map_type.
    def visitMap_type(self, ctx:nasm_x86_64_Parser.Map_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#group.
    def visitGroup(self, ctx:nasm_x86_64_Parser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#uppercase.
    def visitUppercase(self, ctx:nasm_x86_64_Parser.UppercaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#import_rule.
    def visitImport_rule(self, ctx:nasm_x86_64_Parser.Import_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#export.
    def visitExport(self, ctx:nasm_x86_64_Parser.ExportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#export_params.
    def visitExport_params(self, ctx:nasm_x86_64_Parser.Export_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#resident.
    def visitResident(self, ctx:nasm_x86_64_Parser.ResidentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#nodata.
    def visitNodata(self, ctx:nasm_x86_64_Parser.NodataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#parm.
    def visitParm(self, ctx:nasm_x86_64_Parser.ParmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#safeseh.
    def visitSafeseh(self, ctx:nasm_x86_64_Parser.SafesehContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#osabi.
    def visitOsabi(self, ctx:nasm_x86_64_Parser.OsabiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#times_prefix.
    def visitTimes_prefix(self, ctx:nasm_x86_64_Parser.Times_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#times.
    def visitTimes(self, ctx:nasm_x86_64_Parser.TimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#pseudoinstruction.
    def visitPseudoinstruction(self, ctx:nasm_x86_64_Parser.PseudoinstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#dx.
    def visitDx(self, ctx:nasm_x86_64_Parser.DxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#float_number.
    def visitFloat_number(self, ctx:nasm_x86_64_Parser.Float_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#question.
    def visitQuestion(self, ctx:nasm_x86_64_Parser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#resx.
    def visitResx(self, ctx:nasm_x86_64_Parser.ResxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#incbin.
    def visitIncbin(self, ctx:nasm_x86_64_Parser.IncbinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#string.
    def visitString(self, ctx:nasm_x86_64_Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#value.
    def visitValue(self, ctx:nasm_x86_64_Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#atom.
    def visitAtom(self, ctx:nasm_x86_64_Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#size.
    def visitSize(self, ctx:nasm_x86_64_Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#listt.
    def visitListt(self, ctx:nasm_x86_64_Parser.ListtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#duplist.
    def visitDuplist(self, ctx:nasm_x86_64_Parser.DuplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#parlist.
    def visitParlist(self, ctx:nasm_x86_64_Parser.ParlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:nasm_x86_64_Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#unaryOperator.
    def visitUnaryOperator(self, ctx:nasm_x86_64_Parser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#castExpression.
    def visitCastExpression(self, ctx:nasm_x86_64_Parser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:nasm_x86_64_Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:nasm_x86_64_Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#shiftExpression.
    def visitShiftExpression(self, ctx:nasm_x86_64_Parser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:nasm_x86_64_Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#equalityExpression.
    def visitEqualityExpression(self, ctx:nasm_x86_64_Parser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#andExpression.
    def visitAndExpression(self, ctx:nasm_x86_64_Parser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:nasm_x86_64_Parser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:nasm_x86_64_Parser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#booleanAndExpression.
    def visitBooleanAndExpression(self, ctx:nasm_x86_64_Parser.BooleanAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#booleanOrExpression.
    def visitBooleanOrExpression(self, ctx:nasm_x86_64_Parser.BooleanOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#conditionalExpression.
    def visitConditionalExpression(self, ctx:nasm_x86_64_Parser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#expression.
    def visitExpression(self, ctx:nasm_x86_64_Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#equ.
    def visitEqu(self, ctx:nasm_x86_64_Parser.EquContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#instruction.
    def visitInstruction(self, ctx:nasm_x86_64_Parser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#opcode.
    def visitOpcode(self, ctx:nasm_x86_64_Parser.OpcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#operand.
    def visitOperand(self, ctx:nasm_x86_64_Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#register.
    def visitRegister(self, ctx:nasm_x86_64_Parser.RegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#strict.
    def visitStrict(self, ctx:nasm_x86_64_Parser.StrictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#macro_call.
    def visitMacro_call(self, ctx:nasm_x86_64_Parser.Macro_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nasm_x86_64_Parser#macro_param.
    def visitMacro_param(self, ctx:nasm_x86_64_Parser.Macro_paramContext):
        return self.visitChildren(ctx)



def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ASMLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ASMParser(stream)
    tree = parser.program()
    
    visitor = Visitor()
    visitor.visitProgram(tree)
    print(visitor.instructions_list)
    print(visitor.constraints_list)


if __name__ == '__main__':
    main(sys.argv)
