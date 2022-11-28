from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
import sys

a = input('? ')
visitor = EvalVisitor()


while a != '.':

    antlr = InputStream(a)

    lexer = ExprLexer(antlr)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()

    visitor.visit(tree)
    a = input('? ')
