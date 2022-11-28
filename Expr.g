grammar Expr;

root : bloque EOF;

bloque: if | while | statement;

statement : assig
    | expr
    ;

assig : VAR '<-' expr;

if : 'if' cond '{' bloque '}' ?('else' '{' bloque '}') ;

while: 'while' cond '{' statement *statement '}';

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
    ;

NUM : [0-9]+ ;
VAR: [a-z]+ ;
WS : [ \n]+ -> skip ;
GT : '>';
GTE: '>=';
LTE: '<=';
LT : '<';
EQ : '=';
DIF : '!=';
