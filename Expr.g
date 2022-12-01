grammar Expr;

root : func EOF | bloque EOF;

func: ID args '{' bloque '}';

args: VAR*;

bloque: (si|mientras|statement)+;

statement : assig
    | expr
    ;

assig : VAR '<-' expr;

si : 'if' cond '{' bloque '}' ('else' '{' bloque '}')? ;

mientras: 'while' cond '{' bloque '}';

cond : VAR operadorbool VAR  #condVARVAR
    | VAR operadorbool expr  #condVARExpr
    | expr operadorbool expr  #condExprExpr
    ;


operadorbool : GT | LT | EQ | DIF | GTE | LTE;

expr
    : <assoc=right> expr '^' expr  #Potencia
    | expr ('*'|'/') expr  #MulDiv
    | expr ('+'|'-') expr  #SumRes
    | '(' expr ')'  #Paren
    | NUM   #Num
    | VAR #Var
    | ID expr* #Id
    ;

NUM : [0-9]+ ;
ID: [A-Z][a-z]*;
VAR: [a-z]+ ;
WS : [ \n]+ -> skip ;
GT : '>';
GTE: '>=';
LTE: '<=';
LT : '<';
EQ : '=';
DIF : '!=';
