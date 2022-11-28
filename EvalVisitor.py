if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.variables = {}


    def visitRoot(self,ctx):
        l = list(ctx.getChildren())
        if(len(l) == 2):
            print(self.visit(l[0]))

    def visitBloque(self, ctx:ExprParser.BloqueContext):
        return self.visitChildren(ctx)

    def visitIf(self, ctx:ExprParser.IfContext):
        if(self.visit(ctx.cond())):
            return self.visit(ctx.bloque())

    # Visit a parse tree produced by ExprParser#condVARVAR.
    def visitCondVARVAR(self, ctx:ExprParser.CondVARVARContext):
        l = list(ctx.getChildren())
        operador = self.visit(ctx.operadorbool())
        if operador == '>':
            return self.variables[l[0].getText()] > self.variables[l[2].getText()]
        elif operador == '<':
            return self.variables[l[0].getText()] < self.variables[l[2].getText()]
        else:
            return self.variables[l[0].getText()] == self.variables[l[2].getText()]



    # Visit a parse tree produced by ExprParser#condVARExpr.
    def visitCondVARExpr(self, ctx:ExprParser.CondVARExprContext):
        l = list(ctx.getChildren())
        operador = self.visit(ctx.operadorbool())
        if operador == '>':
            return self.variables[l[0].getText()] > self.visit(l[2])
        elif operador == '<':
            return self.variables[l[0].getText()] < self.visit(l[2])
        else:
            return self.variables[l[0].getText()] == self.visit(l[2])


    # Visit a parse tree produced by ExprParser#condExprExpr.
    def visitCondExprExpr(self, ctx:ExprParser.CondExprExprContext):
        l = list(ctx.getChildren())
        operador = self.visit(ctx.operadorbool())
        if operador == '>':
            return self.visit(l[0]) > self.visit(l[2])
        elif operador == '<':
            return self.visit(l[0]) < self.visit(l[2])
        else:
            return self.visit(l[0]) == self.visit(l[2])


    # Visit a parse tree produced by ExprParser#operadorbool.
    def visitOperadorbool(self, ctx:ExprParser.OperadorboolContext):
        return list(ctx.getChildren())[0].getText()

    def visitPotencia(self, ctx):
        l = list(ctx.getChildren())
        return pow(self.visit(l[0]),self.visit(l[2]))

    def visitSumRes(self, ctx):
        l = list(ctx.getChildren())
        if(l[1].getText() == '+'):
            return self.visit(l[0]) + self.visit(l[2])
        else:
            return self.visit(l[0]) - self.visit(l[2])

    def visitMulDiv(self, ctx):
        l = list(ctx.getChildren())
        if(l[1].getText() == '*'):
            return self.visit(l[0]) * self.visit(l[2])
        else:
            return self.visit(l[0]) // self.visit(l[2])

    def visitParen(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    def visitNum(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#assig.
    def visitAssig(self, ctx):
        self.variables[ctx.VAR().getText()] = self.visit(ctx.expr())
        return "Variable "+ ctx.VAR().getText() + " inicializada."

    # Visit a parse tree produced by ExprParser#write.
    def visitWrite(self, ctx):
        return self.variables[ctx.VAR().getText()]
