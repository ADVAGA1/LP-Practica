# Generated from .\funx.g4 by ANTLR 4.11.1
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
        4,1,27,141,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,1,0,3,0,33,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,5,2,42,8,
        2,10,2,12,2,45,9,2,1,3,1,3,1,3,4,3,50,8,3,11,3,12,3,51,1,4,1,4,1,
        4,3,4,57,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,73,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,85,8,
        8,10,8,12,8,88,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,102,8,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,117,8,12,10,12,12,12,120,9,12,3,12,122,8,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,
        136,8,12,10,12,12,12,139,9,12,1,12,0,1,24,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,4,1,0,26,27,1,0,20,25,1,0,8,9,1,0,11,12,146,0,32,
        1,0,0,0,2,34,1,0,0,0,4,43,1,0,0,0,6,49,1,0,0,0,8,56,1,0,0,0,10,58,
        1,0,0,0,12,62,1,0,0,0,14,74,1,0,0,0,16,80,1,0,0,0,18,101,1,0,0,0,
        20,103,1,0,0,0,22,105,1,0,0,0,24,121,1,0,0,0,26,27,3,2,1,0,27,28,
        5,0,0,1,28,33,1,0,0,0,29,30,3,6,3,0,30,31,5,0,0,1,31,33,1,0,0,0,
        32,26,1,0,0,0,32,29,1,0,0,0,33,1,1,0,0,0,34,35,5,16,0,0,35,36,3,
        4,2,0,36,37,5,1,0,0,37,38,3,6,3,0,38,39,5,2,0,0,39,3,1,0,0,0,40,
        42,5,17,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,
        0,0,44,5,1,0,0,0,45,43,1,0,0,0,46,50,3,12,6,0,47,50,3,14,7,0,48,
        50,3,8,4,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,51,1,0,0,
        0,51,49,1,0,0,0,51,52,1,0,0,0,52,7,1,0,0,0,53,57,3,10,5,0,54,57,
        3,24,12,0,55,57,3,18,9,0,56,53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,
        0,57,9,1,0,0,0,58,59,5,17,0,0,59,60,5,3,0,0,60,61,3,24,12,0,61,11,
        1,0,0,0,62,63,5,4,0,0,63,64,3,16,8,0,64,65,5,1,0,0,65,66,3,6,3,0,
        66,72,5,2,0,0,67,68,5,5,0,0,68,69,5,1,0,0,69,70,3,6,3,0,70,71,5,
        2,0,0,71,73,1,0,0,0,72,67,1,0,0,0,72,73,1,0,0,0,73,13,1,0,0,0,74,
        75,5,6,0,0,75,76,3,16,8,0,76,77,5,1,0,0,77,78,3,6,3,0,78,79,5,2,
        0,0,79,15,1,0,0,0,80,86,3,18,9,0,81,82,3,20,10,0,82,83,3,18,9,0,
        83,85,1,0,0,0,84,81,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,
        0,0,0,87,17,1,0,0,0,88,86,1,0,0,0,89,90,5,17,0,0,90,91,3,22,11,0,
        91,92,5,17,0,0,92,102,1,0,0,0,93,94,5,17,0,0,94,95,3,22,11,0,95,
        96,3,24,12,0,96,102,1,0,0,0,97,98,3,24,12,0,98,99,3,22,11,0,99,100,
        3,24,12,0,100,102,1,0,0,0,101,89,1,0,0,0,101,93,1,0,0,0,101,97,1,
        0,0,0,102,19,1,0,0,0,103,104,7,0,0,0,104,21,1,0,0,0,105,106,7,1,
        0,0,106,23,1,0,0,0,107,108,6,12,-1,0,108,109,5,13,0,0,109,110,3,
        24,12,0,110,111,5,14,0,0,111,122,1,0,0,0,112,122,5,15,0,0,113,122,
        5,17,0,0,114,118,5,16,0,0,115,117,3,24,12,0,116,115,1,0,0,0,117,
        120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,122,1,0,0,0,120,
        118,1,0,0,0,121,107,1,0,0,0,121,112,1,0,0,0,121,113,1,0,0,0,121,
        114,1,0,0,0,122,137,1,0,0,0,123,124,10,8,0,0,124,125,5,7,0,0,125,
        136,3,24,12,8,126,127,10,7,0,0,127,128,7,2,0,0,128,136,3,24,12,8,
        129,130,10,6,0,0,130,131,5,10,0,0,131,136,3,24,12,7,132,133,10,5,
        0,0,133,134,7,3,0,0,134,136,3,24,12,6,135,123,1,0,0,0,135,126,1,
        0,0,0,135,129,1,0,0,0,135,132,1,0,0,0,136,139,1,0,0,0,137,135,1,
        0,0,0,137,138,1,0,0,0,138,25,1,0,0,0,139,137,1,0,0,0,12,32,43,49,
        51,56,72,86,101,118,121,135,137
    ]

class funxParser ( Parser ):

    grammarFileName = "funx.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'<-'", "'if'", "'else'", 
                     "'while'", "'^'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'>'", "'>='", "'<='", "'<'", 
                     "'='", "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "VAR", "WS", "COMMENT", "GT", "GTE", "LTE", "LT", 
                      "EQ", "DIF", "AND", "OR" ]

    RULE_root = 0
    RULE_func = 1
    RULE_args = 2
    RULE_bloque = 3
    RULE_statement = 4
    RULE_assig = 5
    RULE_si = 6
    RULE_mientras = 7
    RULE_condicion = 8
    RULE_cond = 9
    RULE_oplogico = 10
    RULE_operadorbool = 11
    RULE_expr = 12

    ruleNames =  [ "root", "func", "args", "bloque", "statement", "assig", 
                   "si", "mientras", "condicion", "cond", "oplogico", "operadorbool", 
                   "expr" ]

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
    AND=26
    OR=27

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
            return self.getTypedRuleContext(funxParser.FuncContext,0)


        def EOF(self):
            return self.getToken(funxParser.EOF, 0)

        def bloque(self):
            return self.getTypedRuleContext(funxParser.BloqueContext,0)


        def getRuleIndex(self):
            return funxParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = funxParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.func()
                self.state = 27
                self.match(funxParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.bloque()
                self.state = 30
                self.match(funxParser.EOF)
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
            return self.getToken(funxParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(funxParser.ArgsContext,0)


        def bloque(self):
            return self.getTypedRuleContext(funxParser.BloqueContext,0)


        def getRuleIndex(self):
            return funxParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = funxParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(funxParser.ID)
            self.state = 35
            self.args()
            self.state = 36
            self.match(funxParser.T__0)
            self.state = 37
            self.bloque()
            self.state = 38
            self.match(funxParser.T__1)
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
                return self.getTokens(funxParser.VAR)
            else:
                return self.getToken(funxParser.VAR, i)

        def getRuleIndex(self):
            return funxParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = funxParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 40
                self.match(funxParser.VAR)
                self.state = 45
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
                return self.getTypedRuleContexts(funxParser.SiContext)
            else:
                return self.getTypedRuleContext(funxParser.SiContext,i)


        def mientras(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.MientrasContext)
            else:
                return self.getTypedRuleContext(funxParser.MientrasContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.StatementContext)
            else:
                return self.getTypedRuleContext(funxParser.StatementContext,i)


        def getRuleIndex(self):
            return funxParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = funxParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 46
                    self.si()
                    pass
                elif token in [6]:
                    self.state = 47
                    self.mientras()
                    pass
                elif token in [13, 15, 16, 17]:
                    self.state = 48
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 51 
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
            return self.getTypedRuleContext(funxParser.AssigContext,0)


        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def cond(self):
            return self.getTypedRuleContext(funxParser.CondContext,0)


        def getRuleIndex(self):
            return funxParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = funxParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.assig()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.cond()
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
            return self.getToken(funxParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def getRuleIndex(self):
            return funxParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = funxParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(funxParser.VAR)
            self.state = 59
            self.match(funxParser.T__2)
            self.state = 60
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

        def condicion(self):
            return self.getTypedRuleContext(funxParser.CondicionContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.BloqueContext)
            else:
                return self.getTypedRuleContext(funxParser.BloqueContext,i)


        def getRuleIndex(self):
            return funxParser.RULE_si

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi" ):
                return visitor.visitSi(self)
            else:
                return visitor.visitChildren(self)




    def si(self):

        localctx = funxParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_si)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(funxParser.T__3)
            self.state = 63
            self.condicion()
            self.state = 64
            self.match(funxParser.T__0)
            self.state = 65
            self.bloque()
            self.state = 66
            self.match(funxParser.T__1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 67
                self.match(funxParser.T__4)
                self.state = 68
                self.match(funxParser.T__0)
                self.state = 69
                self.bloque()
                self.state = 70
                self.match(funxParser.T__1)


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

        def condicion(self):
            return self.getTypedRuleContext(funxParser.CondicionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(funxParser.BloqueContext,0)


        def getRuleIndex(self):
            return funxParser.RULE_mientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientras" ):
                return visitor.visitMientras(self)
            else:
                return visitor.visitChildren(self)




    def mientras(self):

        localctx = funxParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(funxParser.T__5)
            self.state = 75
            self.condicion()
            self.state = 76
            self.match(funxParser.T__0)
            self.state = 77
            self.bloque()
            self.state = 78
            self.match(funxParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.CondContext)
            else:
                return self.getTypedRuleContext(funxParser.CondContext,i)


        def oplogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.OplogicoContext)
            else:
                return self.getTypedRuleContext(funxParser.OplogicoContext,i)


        def getRuleIndex(self):
            return funxParser.RULE_condicion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = funxParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.cond()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 81
                self.oplogico()
                self.state = 82
                self.cond()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return funxParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondVARExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(funxParser.VAR, 0)
        def operadorbool(self):
            return self.getTypedRuleContext(funxParser.OperadorboolContext,0)

        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondVARExpr" ):
                return visitor.visitCondVARExpr(self)
            else:
                return visitor.visitChildren(self)


    class CondExprExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)

        def operadorbool(self):
            return self.getTypedRuleContext(funxParser.OperadorboolContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondExprExpr" ):
                return visitor.visitCondExprExpr(self)
            else:
                return visitor.visitChildren(self)


    class CondVARVARContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(funxParser.VAR)
            else:
                return self.getToken(funxParser.VAR, i)
        def operadorbool(self):
            return self.getTypedRuleContext(funxParser.OperadorboolContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondVARVAR" ):
                return visitor.visitCondVARVAR(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = funxParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cond)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = funxParser.CondVARVARContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(funxParser.VAR)
                self.state = 90
                self.operadorbool()
                self.state = 91
                self.match(funxParser.VAR)
                pass

            elif la_ == 2:
                localctx = funxParser.CondVARExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(funxParser.VAR)
                self.state = 94
                self.operadorbool()
                self.state = 95
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = funxParser.CondExprExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.expr(0)
                self.state = 98
                self.operadorbool()
                self.state = 99
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OplogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(funxParser.AND, 0)

        def OR(self):
            return self.getToken(funxParser.OR, 0)

        def getRuleIndex(self):
            return funxParser.RULE_oplogico

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOplogico" ):
                return visitor.visitOplogico(self)
            else:
                return visitor.visitChildren(self)




    def oplogico(self):

        localctx = funxParser.OplogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_oplogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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


    class OperadorboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(funxParser.GT, 0)

        def LT(self):
            return self.getToken(funxParser.LT, 0)

        def EQ(self):
            return self.getToken(funxParser.EQ, 0)

        def DIF(self):
            return self.getToken(funxParser.DIF, 0)

        def GTE(self):
            return self.getToken(funxParser.GTE, 0)

        def LTE(self):
            return self.getToken(funxParser.LTE, 0)

        def getRuleIndex(self):
            return funxParser.RULE_operadorbool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorbool" ):
                return visitor.visitOperadorbool(self)
            else:
                return visitor.visitChildren(self)




    def operadorbool(self):

        localctx = funxParser.OperadorboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operadorbool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
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
            return funxParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumResContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumRes" ):
                return visitor.visitSumRes(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(funxParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ModuloContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(funxParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(funxParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class PotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(funxParser.ExprContext)
            else:
                return self.getTypedRuleContext(funxParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a funxParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(funxParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = funxParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = funxParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 108
                self.match(funxParser.T__12)
                self.state = 109
                self.expr(0)
                self.state = 110
                self.match(funxParser.T__13)
                pass
            elif token in [15]:
                localctx = funxParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(funxParser.NUM)
                pass
            elif token in [17]:
                localctx = funxParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(funxParser.VAR)
                pass
            elif token in [16]:
                localctx = funxParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(funxParser.ID)
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 115
                        self.expr(0) 
                    self.state = 120
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 135
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = funxParser.PotenciaContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 124
                        self.match(funxParser.T__6)
                        self.state = 125
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = funxParser.MulDivContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 127
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = funxParser.ModuloContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 130
                        self.match(funxParser.T__9)
                        self.state = 131
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = funxParser.SumResContext(self, funxParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 133
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        self.expr(6)
                        pass

             
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self._predicates[12] = self.expr_sempred
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
         




