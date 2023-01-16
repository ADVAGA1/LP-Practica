# Generated from .\funx.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .funxParser import funxParser
else:
    from funxParser import funxParser

# This class defines a complete generic visitor for a parse tree produced by funxParser.

class funxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by funxParser#root.
    def visitRoot(self, ctx:funxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#func.
    def visitFunc(self, ctx:funxParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#args.
    def visitArgs(self, ctx:funxParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#bloque.
    def visitBloque(self, ctx:funxParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#statement.
    def visitStatement(self, ctx:funxParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#assig.
    def visitAssig(self, ctx:funxParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#si.
    def visitSi(self, ctx:funxParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#mientras.
    def visitMientras(self, ctx:funxParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#condicion.
    def visitCondicion(self, ctx:funxParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#condVARVAR.
    def visitCondVARVAR(self, ctx:funxParser.CondVARVARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#condVARExpr.
    def visitCondVARExpr(self, ctx:funxParser.CondVARExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#condExprExpr.
    def visitCondExprExpr(self, ctx:funxParser.CondExprExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#oplogico.
    def visitOplogico(self, ctx:funxParser.OplogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#operadorbool.
    def visitOperadorbool(self, ctx:funxParser.OperadorboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#SumRes.
    def visitSumRes(self, ctx:funxParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#MulDiv.
    def visitMulDiv(self, ctx:funxParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Var.
    def visitVar(self, ctx:funxParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Modulo.
    def visitModulo(self, ctx:funxParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Num.
    def visitNum(self, ctx:funxParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Id.
    def visitId(self, ctx:funxParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Potencia.
    def visitPotencia(self, ctx:funxParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by funxParser#Paren.
    def visitParen(self, ctx:funxParser.ParenContext):
        return self.visitChildren(ctx)



del funxParser