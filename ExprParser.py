# Generated from .\Expr.g by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,3,1,25,8,1,1,2,1,2,3,2,
        29,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,40,8,4,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,71,8,6,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,82,8,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,0,1,16,9,0,2,4,6,8,
        10,12,14,16,0,3,1,0,17,22,1,0,8,9,1,0,10,11,100,0,18,1,0,0,0,2,24,
        1,0,0,0,4,28,1,0,0,0,6,30,1,0,0,0,8,34,1,0,0,0,10,46,1,0,0,0,12,
        70,1,0,0,0,14,72,1,0,0,0,16,81,1,0,0,0,18,19,3,2,1,0,19,20,5,0,0,
        1,20,1,1,0,0,0,21,25,3,8,4,0,22,25,3,10,5,0,23,25,3,4,2,0,24,21,
        1,0,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,0,26,29,3,6,3,0,27,
        29,3,16,8,0,28,26,1,0,0,0,28,27,1,0,0,0,29,5,1,0,0,0,30,31,5,15,
        0,0,31,32,5,1,0,0,32,33,3,16,8,0,33,7,1,0,0,0,34,35,5,2,0,0,35,36,
        3,12,6,0,36,37,5,3,0,0,37,39,3,2,1,0,38,40,5,4,0,0,39,38,1,0,0,0,
        39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,5,0,0,42,43,5,3,0,0,43,44,3,
        2,1,0,44,45,5,4,0,0,45,9,1,0,0,0,46,47,5,6,0,0,47,48,3,12,6,0,48,
        52,5,3,0,0,49,51,3,4,2,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,3,4,2,0,56,57,
        5,4,0,0,57,11,1,0,0,0,58,59,5,15,0,0,59,60,3,14,7,0,60,61,5,15,0,
        0,61,71,1,0,0,0,62,63,5,15,0,0,63,64,3,14,7,0,64,65,3,16,8,0,65,
        71,1,0,0,0,66,67,3,16,8,0,67,68,3,14,7,0,68,69,3,16,8,0,69,71,1,
        0,0,0,70,58,1,0,0,0,70,62,1,0,0,0,70,66,1,0,0,0,71,13,1,0,0,0,72,
        73,7,0,0,0,73,15,1,0,0,0,74,75,6,8,-1,0,75,76,5,12,0,0,76,77,3,16,
        8,0,77,78,5,13,0,0,78,82,1,0,0,0,79,82,5,14,0,0,80,82,5,15,0,0,81,
        74,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,94,1,0,0,0,83,84,10,6,
        0,0,84,85,5,7,0,0,85,93,3,16,8,6,86,87,10,5,0,0,87,88,7,1,0,0,88,
        93,3,16,8,6,89,90,10,4,0,0,90,91,7,2,0,0,91,93,3,16,8,5,92,83,1,
        0,0,0,92,86,1,0,0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,
        95,1,0,0,0,95,17,1,0,0,0,96,94,1,0,0,0,8,24,28,39,52,70,81,92,94
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'if'", "'{'", "'}'", "'else'", 
                     "'while'", "'^'", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "'>'", 
                     "'>='", "'<='", "'<'", "'='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "VAR", "WS", "GT", 
                      "GTE", "LTE", "LT", "EQ", "DIF" ]

    RULE_root = 0
    RULE_bloque = 1
    RULE_statement = 2
    RULE_assig = 3
    RULE_if = 4
    RULE_while = 5
    RULE_cond = 6
    RULE_operadorbool = 7
    RULE_expr = 8

    ruleNames =  [ "root", "bloque", "statement", "assig", "if", "while", 
                   "cond", "operadorbool", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    NUM=14
    VAR=15
    WS=16
    GT=17
    GTE=18
    LTE=19
    LT=20
    EQ=21
    DIF=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.bloque()
            self.state = 19
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(ExprParser.IfContext,0)


        def while_(self):
            return self.getTypedRuleContext(ExprParser.WhileContext,0)


        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = ExprParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloque)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.if_()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.while_()
                pass
            elif token in [12, 14, 15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assig(self):
            return self.getTypedRuleContext(ExprParser.AssigContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.assig()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = ExprParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ExprParser.VAR)
            self.state = 31
            self.match(ExprParser.T__0)
            self.state = 32
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BloqueContext)
            else:
                return self.getTypedRuleContext(ExprParser.BloqueContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = ExprParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ExprParser.T__1)
            self.state = 35
            self.cond()
            self.state = 36
            self.match(ExprParser.T__2)
            self.state = 37
            self.bloque()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 38
                self.match(ExprParser.T__3)


            self.state = 41
            self.match(ExprParser.T__4)
            self.state = 42
            self.match(ExprParser.T__2)
            self.state = 43
            self.bloque()
            self.state = 44
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = ExprParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExprParser.T__5)
            self.state = 47
            self.cond()
            self.state = 48
            self.match(ExprParser.T__2)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self.statement() 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 55
            self.statement()
            self.state = 56
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondVARExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)
        def operadorbool(self):
            return self.getTypedRuleContext(ExprParser.OperadorboolContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondVARExpr" ):
                return visitor.visitCondVARExpr(self)
            else:
                return visitor.visitChildren(self)


    class CondExprExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def operadorbool(self):
            return self.getTypedRuleContext(ExprParser.OperadorboolContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondExprExpr" ):
                return visitor.visitCondExprExpr(self)
            else:
                return visitor.visitChildren(self)


    class CondVARVARContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VAR)
            else:
                return self.getToken(ExprParser.VAR, i)
        def operadorbool(self):
            return self.getTypedRuleContext(ExprParser.OperadorboolContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondVARVAR" ):
                return visitor.visitCondVARVAR(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = ExprParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cond)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.CondVARVARContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ExprParser.VAR)
                self.state = 59
                self.operadorbool()
                self.state = 60
                self.match(ExprParser.VAR)
                pass

            elif la_ == 2:
                localctx = ExprParser.CondVARExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(ExprParser.VAR)
                self.state = 63
                self.operadorbool()
                self.state = 64
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.CondExprExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.operadorbool()
                self.state = 68
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(ExprParser.GT, 0)

        def LT(self):
            return self.getToken(ExprParser.LT, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def DIF(self):
            return self.getToken(ExprParser.DIF, 0)

        def GTE(self):
            return self.getToken(ExprParser.GTE, 0)

        def LTE(self):
            return self.getToken(ExprParser.LTE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_operadorbool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorbool" ):
                return visitor.visitOperadorbool(self)
            else:
                return visitor.visitChildren(self)




    def operadorbool(self):

        localctx = ExprParser.OperadorboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operadorbool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumResContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumRes" ):
                return visitor.visitSumRes(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class PotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = ExprParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 75
                self.match(ExprParser.T__11)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(ExprParser.T__12)
                pass
            elif token in [14]:
                localctx = ExprParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(ExprParser.NUM)
                pass
            elif token in [15]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(ExprParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.PotenciaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 84
                        self.match(ExprParser.T__6)
                        self.state = 85
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulDivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 87
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.SumResContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 90
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(5)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




