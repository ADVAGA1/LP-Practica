grammar Expr;

root : func EOF | bloque EOF;

func: ID args '{' bloque '}';

args: VAR*;

bloque: (si|mientras|statement)+;

statement : assig
    | expr
    | cond
    ;

assig : VAR '<-' expr;

si : 'if' condicion '{' bloque '}' ('else' '{' bloque '}')? ;

mientras: 'while' cond '{' bloque '}';

condicion: cond (oplogico cond)*;

cond : VAR operadorbool VAR  #condVARVAR
    | VAR operadorbool expr  #condVARExpr
    | expr operadorbool expr  #condExprExpr
    ;

oplogico : AND | OR;

operadorbool : GT | LT | EQ | DIF | GTE | LTE;

expr
    : <assoc=right> expr '^' expr  #Potencia
    | expr ('*'|'/') expr  #MulDiv
    | expr '%' expr        #Modulo
    | expr ('+'|'-') expr  #SumRes
    | '(' expr ')'  #Paren
    | NUM   #Num
    | VAR #Var
    | ID expr* #Id
    ;

NUM : [0-9]+ ;
ID: [A-Z]+[a-zA-Z0-9]*;
VAR: [a-z]+ ;
WS : [ \n\r]+ -> skip ;
COMMENT: '#'[ a-zA-Z0-9]* -> skip;
GT : '>';
GTE: '>=';
LTE: '<=';
LT : '<';
EQ : '=';
DIF : '!=';
AND: '&&';
OR: '||';
