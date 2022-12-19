if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.stack_variables = [{}]
        self.functions = {}   #clave ID, valores PARAMS, CONTEXT


    def visitRoot(self,ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    # Visit a parse tree produced by ExprParser#def.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        l = list(ctx.getChildren())
        assert not l[0].getText() in self.functions, "Error: Funcion ya definida"
        f_info = {}
        f_info["PARAMS"] = []
        params = self.visit(l[1])
        for i in params:
            assert not i in f_info["PARAMS"], "Error: parametros repetidos"
            f_info["PARAMS"].append(i)
        f_info["CONTEXT"] = l[-2]
        self.functions[l[0].getText()] = f_info

    # Visit a parse tree produced by ExprParser#args.
    def visitArgs(self, ctx:ExprParser.ArgsContext):
        l = list(ctx.getChildren())
        lista = []
        for child in l:
            lista.append(child.getText())
        return lista

    def visitBloque(self, ctx:ExprParser.BloqueContext):
        l = list(ctx.getChildren())
        for child in l:
            n = self.visit(child)
            if n is not None: return n

    # Visit a parse tree produced by ExprParser#while.
    def visitMientras(self, ctx:ExprParser.MientrasContext):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            for i in range(3, len(l)-1):
                n = self.visit(l[i])
                if n is not None: return n

    def visitSi(self, ctx:ExprParser.SiContext):
        l = list(ctx.getChildren())
        if(len(l) == 5):
            if(self.visit(l[1])):
                n = self.visit(l[3])
                if n is not None: return n
        else:
            if(self.visit(l[1])):
                n = self.visit(l[3])
                if n is not None: return n
            else:
                n = self.visit(l[7])
                if n is not None: return n

    # Visit a parse tree produced by ExprParser#condVARVAR.
    def visitCondVARVAR(self, ctx:ExprParser.CondVARVARContext):
        l = list(ctx.getChildren())
        operador = self.visit(ctx.operadorbool())
        if operador == '>':
            return self.stack_variables[-1][l[0].getText()] > self.stack_variables[-1][l[2].getText()]
        elif operador == '<':
            return self.stack_variables[-1][l[0].getText()] < self.stack_variables[-1][l[2].getText()]
        elif operador == '<=':
            return self.stack_variables[-1][l[0].getText()] <= self.stack_variables[-1][l[2].getText()]
        elif operador == '>=':
            return self.stack_variables[-1][l[0].getText()] >= self.stack_variables[-1][l[2].getText()]
        elif operador == '!=':
            return self.stack_variables[-1][l[0].getText()] != self.stack_variables[-1][l[2].getText()]
        else:
            return self.stack_variables[-1][l[0].getText()] == self.stack_variables[-1][l[2].getText()]



    # Visit a parse tree produced by ExprParser#condVARExpr.
    def visitCondVARExpr(self, ctx:ExprParser.CondVARExprContext):
        l = list(ctx.getChildren())
        operador = self.visit(ctx.operadorbool())
        if operador == '>':
            return self.stack_variables[-1][l[0].getText()] > self.visit(l[2])
        elif operador == '<':
            return self.stack_variables[-1][l[0].getText()] < self.visit(l[2])
        elif operador == '<=':
            return self.stack_variables[-1][l[0].getText()] <= self.visit(l[2])
        elif operador == '>=':
            return self.stack_variables[-1][l[0].getText()] >= self.visit(l[2])
        elif operador == '!=':
            return self.stack_variables[-1][l[0].getText()] != self.visit(l[2])
        else:
            return self.stack_variables[-1][l[0].getText()] == self.visit(l[2])


    # Visit a parse tree produced by ExprParser#condExprExpr.
    def visitCondExprExpr(self, ctx:ExprParser.CondExprExprContext):
        l = list(ctx.getChildren())
        operador = self.visit(ctx.operadorbool())
        if operador == '>':
            return self.visit(l[0]) > self.visit(l[2])
        elif operador == '<':
            return self.visit(l[0]) < self.visit(l[2])
        elif operador == '<=':
            return self.visit(l[0]) <= self.visit(l[2])
        elif operador == '>=':
            return self.visit(l[0]) >= self.visit(l[2])
        elif operador == '!=':
            return self.visit(l[0]) != self.visit(l[2])
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
            assert self.visit(l[2]) != 0, "Error: Division por 0"
            return self.visit(l[0]) // self.visit(l[2])

    # Visit a parse tree produced by ExprParser#Modulo.
    def visitModulo(self, ctx:ExprParser.ModuloContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) % self.visit(l[2])

    def visitParen(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    def visitNum(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    # Visit a parse tree produced by ExprParser#Var.
    def visitVar(self, ctx:ExprParser.VarContext):
        l = list(ctx.getChildren())
        return self.stack_variables[-1][l[0].getText()]

    def visitStatement(self, ctx):
        n = self.visitChildren(ctx)
        return n

    # Visit a parse tree produced by ExprParser#assig.
    def visitAssig(self, ctx):
        self.stack_variables[-1][ctx.VAR().getText()] = self.visit(ctx.expr())

    # Visit a parse tree produced by ExprParser#Id.
    def visitId(self, ctx:ExprParser.IdContext):
        l = list(ctx.getChildren())
        assert l[0].getText() in self.functions, "Error: Funcion no definida"
        assert len(l) - 1  == len(self.functions[l[0].getText()]["PARAMS"]), "Error: Numero de parámetros incorrecto"
        variables = {}
        for i in range(0, len(self.functions[l[0].getText()]["PARAMS"])):
            variables[self.functions[l[0].getText()]["PARAMS"][i]] = self.visit(l[i+1])
        self.stack_variables.append(variables)
        ret = self.visit(self.functions[l[0].getText()]["CONTEXT"])
        self.stack_variables.pop()
        return ret
