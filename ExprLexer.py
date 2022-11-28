# Generated from .\Expr.g by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,18,95,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,
        4,12,74,8,12,11,12,12,12,75,1,13,4,13,79,8,13,11,13,12,13,80,1,14,
        4,14,84,8,14,11,14,12,14,85,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,
        17,0,0,18,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,1,0,3,1,0,97,122,1,0,48,57,
        2,0,10,10,32,32,97,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,
        0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,
        0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,1,37,1,0,0,
        0,3,40,1,0,0,0,5,46,1,0,0,0,7,49,1,0,0,0,9,54,1,0,0,0,11,58,1,0,
        0,0,13,60,1,0,0,0,15,62,1,0,0,0,17,64,1,0,0,0,19,66,1,0,0,0,21,68,
        1,0,0,0,23,70,1,0,0,0,25,73,1,0,0,0,27,78,1,0,0,0,29,83,1,0,0,0,
        31,89,1,0,0,0,33,91,1,0,0,0,35,93,1,0,0,0,37,38,5,58,0,0,38,39,5,
        61,0,0,39,2,1,0,0,0,40,41,5,119,0,0,41,42,5,114,0,0,42,43,5,105,
        0,0,43,44,5,116,0,0,44,45,5,101,0,0,45,4,1,0,0,0,46,47,5,105,0,0,
        47,48,5,102,0,0,48,6,1,0,0,0,49,50,5,116,0,0,50,51,5,104,0,0,51,
        52,5,101,0,0,52,53,5,110,0,0,53,8,1,0,0,0,54,55,5,101,0,0,55,56,
        5,110,0,0,56,57,5,100,0,0,57,10,1,0,0,0,58,59,5,94,0,0,59,12,1,0,
        0,0,60,61,5,42,0,0,61,14,1,0,0,0,62,63,5,47,0,0,63,16,1,0,0,0,64,
        65,5,43,0,0,65,18,1,0,0,0,66,67,5,45,0,0,67,20,1,0,0,0,68,69,5,40,
        0,0,69,22,1,0,0,0,70,71,5,41,0,0,71,24,1,0,0,0,72,74,7,0,0,0,73,
        72,1,0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,26,1,0,0,
        0,77,79,7,1,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,
        1,0,0,0,81,28,1,0,0,0,82,84,7,2,0,0,83,82,1,0,0,0,84,85,1,0,0,0,
        85,83,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,6,14,0,0,88,30,1,
        0,0,0,89,90,5,62,0,0,90,32,1,0,0,0,91,92,5,60,0,0,92,34,1,0,0,0,
        93,94,5,61,0,0,94,36,1,0,0,0,4,0,75,80,85,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    VAR = 13
    NUM = 14
    WS = 15
    GT = 16
    LT = 17
    EQ = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'write'", "'if'", "'then'", "'end'", "'^'", "'*'", 
            "'/'", "'+'", "'-'", "'('", "')'", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NUM", "WS", "GT", "LT", "EQ" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "VAR", "NUM", 
                  "WS", "GT", "LT", "EQ" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


