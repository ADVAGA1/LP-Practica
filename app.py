from flask import Flask, render_template, request
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

app = Flask(__name__)
visitor = EvalVisitor()

resultado = []
funciones = []
expr = []

def extender(var):
    p = ""
    for s in var:
        p += s
        p += " "
    return p

def depurar(ins: str) -> str:
    if ins[0] == "#":
        lineas = ins.splitlines()
        lineas.pop(0)
        nins = extender(lineas)
        return depurar(nins)
    return ins


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods = ["POST","GET"])
def result():
    if request.method == "POST":
        result = request.form
        instruccion = result["input"]
        if len(instruccion) == 0:
            return render_template("result.html",result = resultado, funcion = funciones, expresion = expr)
        antlr = InputStream(instruccion)
        lexer = ExprLexer(antlr)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.root()
        try:
            dep = depurar(instruccion)
            expr.append(dep)
            res = visitor.visit(tree)
            if dep[0].isupper():
                try:
                    ind = dep.index("{")
                    funciones.append(dep[0:ind]) 
                except:
                    None   
            resultado.append(res)
        except AssertionError as ex:
            resultado.append(ex.args[0])
        return render_template("result.html",result = resultado, funcion = funciones, expresion = expr)

