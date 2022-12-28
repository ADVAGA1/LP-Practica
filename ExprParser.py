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
        4,1,25,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,0,3,0,
        29,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,5,2,38,8,2,10,2,12,2,41,9,2,1,
        3,1,3,1,3,4,3,46,8,3,11,3,12,3,47,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,68,8,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,88,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,
        10,101,8,10,10,10,12,10,104,9,10,3,10,106,8,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,120,8,10,10,10,12,
        10,123,9,10,1,10,0,1,20,11,0,2,4,6,8,10,12,14,16,18,20,0,3,1,0,20,
        25,1,0,8,9,1,0,11,12,130,0,28,1,0,0,0,2,30,1,0,0,0,4,39,1,0,0,0,
        6,45,1,0,0,0,8,51,1,0,0,0,10,53,1,0,0,0,12,57,1,0,0,0,14,69,1,0,
        0,0,16,87,1,0,0,0,18,89,1,0,0,0,20,105,1,0,0,0,22,23,3,2,1,0,23,
        24,5,0,0,1,24,29,1,0,0,0,25,26,3,6,3,0,26,27,5,0,0,1,27,29,1,0,0,
        0,28,22,1,0,0,0,28,25,1,0,0,0,29,1,1,0,0,0,30,31,5,16,0,0,31,32,
        3,4,2,0,32,33,5,1,0,0,33,34,3,6,3,0,34,35,5,2,0,0,35,3,1,0,0,0,36,
        38,5,17,0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,
        0,0,40,5,1,0,0,0,41,39,1,0,0,0,42,46,3,12,6,0,43,46,3,14,7,0,44,
        46,3,8,4,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,47,1,0,0,
        0,47,45,1,0,0,0,47,48,1,0,0,0,48,7,1,0,0,0,49,52,3,10,5,0,50,52,
        3,20,10,0,51,49,1,0,0,0,51,50,1,0,0,0,52,9,1,0,0,0,53,54,5,17,0,
        0,54,55,5,3,0,0,55,56,3,20,10,0,56,11,1,0,0,0,57,58,5,4,0,0,58,59,
        3,16,8,0,59,60,5,1,0,0,60,61,3,6,3,0,61,67,5,2,0,0,62,63,5,5,0,0,
        63,64,5,1,0,0,64,65,3,6,3,0,65,66,5,2,0,0,66,68,1,0,0,0,67,62,1,
        0,0,0,67,68,1,0,0,0,68,13,1,0,0,0,69,70,5,6,0,0,70,71,3,16,8,0,71,
        72,5,1,0,0,72,73,3,6,3,0,73,74,5,2,0,0,74,15,1,0,0,0,75,76,5,17,
        0,0,76,77,3,18,9,0,77,78,5,17,0,0,78,88,1,0,0,0,79,80,5,17,0,0,80,
        81,3,18,9,0,81,82,3,20,10,0,82,88,1,0,0,0,83,84,3,20,10,0,84,85,
        3,18,9,0,85,86,3,20,10,0,86,88,1,0,0,0,87,75,1,0,0,0,87,79,1,0,0,
        0,87,83,1,0,0,0,88,17,1,0,0,0,89,90,7,0,0,0,90,19,1,0,0,0,91,92,
        6,10,-1,0,92,93,5,13,0,0,93,94,3,20,10,0,94,95,5,14,0,0,95,106,1,
        0,0,0,96,106,5,15,0,0,97,106,5,17,0,0,98,102,5,16,0,0,99,101,3,20,
        10,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,
        0,0,103,106,1,0,0,0,104,102,1,0,0,0,105,91,1,0,0,0,105,96,1,0,0,
        0,105,97,1,0,0,0,105,98,1,0,0,0,106,121,1,0,0,0,107,108,10,8,0,0,
        108,109,5,7,0,0,109,120,3,20,10,8,110,111,10,7,0,0,111,112,7,1,0,
        0,112,120,3,20,10,8,113,114,10,6,0,0,114,115,5,10,0,0,115,120,3,
        20,10,7,116,117,10,5,0,0,117,118,7,2,0,0,118,120,3,20,10,6,119,107,
        1,0,0,0,119,110,1,0,0,0,119,113,1,0,0,0,119,116,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,121,1,
        0,0,0,11,28,39,45,47,51,67,87,102,105,119,121
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'<-'", "'if'", "'else'", 
                     "'while'", "'^'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'>'", "'>='", "'<='", "'<'", 
                     "'='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "VAR", "WS", "COMMENT", "GT", "GTE", "LTE", "LT", 
                      "EQ", "DIF" ]

    RULE_root = 0
    RULE_func = 1
    RULE_args = 2
    RULE_bloque = 3
    RULE_statement = 4
    RULE_assig = 5
    RULE_si = 6
    RULE_mientras = 7
    RULE_cond = 8
    RULE_operadorbool = 9
    RULE_expr = 10

    ruleNames =  [ "root", "func", "args", "bloque", "statement", "assig", 
                   "si", "mientras", "cond", "operadorbool", "expr" ]

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
    T__13=14
    NUM=15
    ID=16
    VAR=17
    WS=18
    COMMENT=19
    GT=20
    GTE=21
    LTE=22
    LT=23
    EQ=24
    DIF=25

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

        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.func()
                self.state = 23
                self.match(ExprParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.bloque()
                self.state = 26
                self.match(ExprParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(ExprParser.ArgsContext,0)


        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ExprParser.ID)
            self.state = 31
            self.args()
            self.state = 32
            self.match(ExprParser.T__0)
            self.state = 33
            self.bloque()
            self.state = 34
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VAR)
            else:
                return self.getToken(ExprParser.VAR, i)

        def getRuleIndex(self):
            return ExprParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ExprParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 36
                self.match(ExprParser.VAR)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def si(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SiContext)
            else:
                return self.getTypedRuleContext(ExprParser.SiContext,i)


        def mientras(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MientrasContext)
            else:
                return self.getTypedRuleContext(ExprParser.MientrasContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = ExprParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 42
                    self.si()
                    pass
                elif token in [6]:
                    self.state = 43
                    self.mientras()
                    pass
                elif token in [13, 15, 16, 17]:
                    self.state = 44
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 237648) != 0):
                    break

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
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.assig()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
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
        self.enterRule(localctx, 10, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExprParser.VAR)
            self.state = 54
            self.match(ExprParser.T__2)
            self.state = 55
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SiContext(ParserRuleContext):
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
            return ExprParser.RULE_si

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi" ):
                return visitor.visitSi(self)
            else:
                return visitor.visitChildren(self)




    def si(self):

        localctx = ExprParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_si)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.T__3)
            self.state = 58
            self.cond()
            self.state = 59
            self.match(ExprParser.T__0)
            self.state = 60
            self.bloque()
            self.state = 61
            self.match(ExprParser.T__1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 62
                self.match(ExprParser.T__4)
                self.state = 63
                self.match(ExprParser.T__0)
                self.state = 64
                self.bloque()
                self.state = 65
                self.match(ExprParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)


        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_mientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientras" ):
                return visitor.visitMientras(self)
            else:
                return visitor.visitChildren(self)




    def mientras(self):

        localctx = ExprParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ExprParser.T__5)
            self.state = 70
            self.cond()
            self.state = 71
            self.match(ExprParser.T__0)
            self.state = 72
            self.bloque()
            self.state = 73
            self.match(ExprParser.T__1)
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
        self.enterRule(localctx, 16, self.RULE_cond)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.CondVARVARContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(ExprParser.VAR)
                self.state = 76
                self.operadorbool()
                self.state = 77
                self.match(ExprParser.VAR)
                pass

            elif la_ == 2:
                localctx = ExprParser.CondVARExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(ExprParser.VAR)
                self.state = 80
                self.operadorbool()
                self.state = 81
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.CondExprExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.operadorbool()
                self.state = 85
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
        self.enterRule(localctx, 18, self.RULE_operadorbool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0):
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


    class ModuloContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
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


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = ExprParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 92
                self.match(ExprParser.T__12)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(ExprParser.T__13)
                pass
            elif token in [15]:
                localctx = ExprParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(ExprParser.NUM)
                pass
            elif token in [17]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(ExprParser.VAR)
                pass
            elif token in [16]:
                localctx = ExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(ExprParser.ID)
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 99
                        self.expr(0) 
                    self.state = 104
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.PotenciaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 108
                        self.match(ExprParser.T__6)
                        self.state = 109
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulDivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 111
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ModuloContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 114
                        self.match(ExprParser.T__9)
                        self.state = 115
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.SumResContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 117
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expr(6)
                        pass

             
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




