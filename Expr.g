grammar Expr;

root : bloque root
    | EOF
    ;

bloque: if | statement;

statement : assig
    | write
    | expr
    ;

assig : VAR ':=' expr;

write : 'write' VAR;

if : 'if' cond 'then' bloque 'end';

cond : VAR operadorbool VAR  #condVARVAR
    | VAR operadorbool expr  #condVARExpr
    | expr operadorbool expr  #condExprExpr
    ;


operadorbool : GT | LT | EQ ;

VAR: [a-z]+ ;

expr
    : <assoc=right> expr '^' expr  #Potencia
    | expr ('*'|'/') expr  #MulDiv
    | expr ('+'|'-') expr  #SumRes
    | '(' expr ')'  #Paren
    | NUM   #Num
    ;

NUM : [0-9]+ ;
WS : [ \n]+ -> skip ;
GT : '>';
LT : '<';
EQ : '=';
