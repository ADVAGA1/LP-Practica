# Generated from .\Expr.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#args.
    def visitArgs(self, ctx:ExprParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx:ExprParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assig.
    def visitAssig(self, ctx:ExprParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#si.
    def visitSi(self, ctx:ExprParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mientras.
    def visitMientras(self, ctx:ExprParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condVARVAR.
    def visitCondVARVAR(self, ctx:ExprParser.CondVARVARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condVARExpr.
    def visitCondVARExpr(self, ctx:ExprParser.CondVARExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condExprExpr.
    def visitCondExprExpr(self, ctx:ExprParser.CondExprExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operadorbool.
    def visitOperadorbool(self, ctx:ExprParser.OperadorboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SumRes.
    def visitSumRes(self, ctx:ExprParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Var.
    def visitVar(self, ctx:ExprParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Num.
    def visitNum(self, ctx:ExprParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Id.
    def visitId(self, ctx:ExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Potencia.
    def visitPotencia(self, ctx:ExprParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Paren.
    def visitParen(self, ctx:ExprParser.ParenContext):
        return self.visitChildren(ctx)



del ExprParser