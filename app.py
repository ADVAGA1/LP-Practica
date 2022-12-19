from flask import Flask, render_template, request
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

app = Flask(__name__)
visitor = EvalVisitor()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/result",methods = ["POST","GET"])
def result():
    if request.method == "POST":
        result = request.form
        antlr = InputStream(result["input"])
        lexer = ExprLexer(antlr)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.root()
        try:
            res = visitor.visit(tree)
        except AssertionError as ex:
            print(ex)
        return render_template("result.html",result = res)

