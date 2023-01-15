# Funx (Práctica LP 2022-2023)

Funx es un lenguaje de programación interpretado en Python orientado a expresiones y funciones. Es un lenguaje muy simple que solo trabaja con números enteros. Tiene operaciones entre expresiones, condicionales, bucles y se pueden declarar funciones.

# Instalación
Funx depende de 3 librerías:
- `ANTLR`
- `flask`
- `jinja`

Entonces para que se pueda ejecutar un programa en Funx se tienen que instalar las anteriores librerías. Se pueden instalar en Linux con los siguientes comandos:

```bash
pip3 install antlr4-python3-runtime==4.7
pip install flask
pip install Jinja2
```
## Invocación del intérprete
Una vez instaladas las librerías necesitamos generar los los árboles abstractos de sintaxis con `ANTLR` en el mismo directorio de donde hayamos descargado los archivos. Esto se hace con el siguiente comando:
```bash
antlr -Dlanguage=Python3 -no-listener -visitor .\funx.g4
```

Una vez ejecutado este comando solo tendremos que preparar el servidor con `flask`. Esto se hace con los siguientes comandos: 
```bash
export FLASK_APP=funx
flask run
```
Esto iniciará un servidor en `localhost`.

Por último tendremos que abrir el archivo `base.html` y listo.

# Introducción al lenguaje
Con Funx se puede evaluar expresiones:

```
# expresiones:

3 + 4 * 2
```
```
Out: 11
```

Como se puede ver, la salida del programa es el resultado de la evaluación de la expresión. Los comentarios se encuentran después del símbolo `#`.

En Funx solo se pueden definir expresiones y funciones.

## Funciones
Cada función tiene un nombre, parámetros y un bloque asociado. Los bloques se encuentran inscritos entre los símbolos `{` y `}`.

Las funciones tienen que empezar con una letra mayúscula. Las variables, en cambio, están en minúscula.

Las funciones pasan los parámetros por copia. Devuelven el valor de cualquier expresión que encuentren en su bloque y en ese preciso instante. Aquí tenéis un ejemplo:

```
# función que recibe dos números enteros y devuelve su suma
Suma x y
{
  x + y
}

Suma (2 * 3) 4 
```
```
Out: 10
```

Esto implica que si encontramos más de una expresión en una función tendremos más de un punto de salida de la función.

Funx permite también la recursividad. Aquí tenéis un ejemplo:
```
Fibo n
{
    if n < 2 { n }
    (Fibo n-1) + (Fibo n-2)
}

Fibo 4
```
```
Out: 3
```
Las variables son locales en cada invocación de cada función y las funciones se pueden comunicar a través de parámetros. Las funciones listan los nombres de sus parámetros formales pero no incluyen su tipo. Los parámetros se separan con espacios.

Mirad el siguiente ejemplo:
```
# funció que rep dos enters i en torna el seu maxim comu divisor

Euclides a b
{
  while a != b
  {
    if a > b 
    {
      a <- a - b
    }
    else
    {
      b <- b - a
    }
  }
  a
}

Euclides 6 8
```

```
Out: 2
```
Las variables no tienen que ser declaradas, todas serán de tipo entero.

Las funciones pueden no tener parámetros. Podemos definir de esta manera funciones constantes:
```
DOS { 2 }
Suma2 x { DOS + x }
Suma2 3
```
```
Out: 5
```
Si una función no tiene ninguna expresión no devolverá nada.

Si 

## Especificación de Funx
Las instrucciones de Funx son:
- la asignación con `<-`,
- la invocación de funciones,
- el condicional con `if` y posible `else`,
- el bucle con `while`

Las instrucciones escritas una detrás de la otra se ejecutan secuencialmente.

### Asignación
La asignación evalúa primero la expresión de la parte derecha del `<-` y guarda el resultado en la variable local de la parte izquierda.

Ejemplo: `a <- a - b`

La asignación no devuelve nada.

### Condicional
La instrucción condicional tiene la semántica habitual. El bloque del `else` es optativo.

Ejemplo: `if x = y { z <- 1 }` i `if x = y { z <- 1 } else { z <- 2 }`.

Los limitadores de los bloques son siempre obligatorios.

Los operadores relacionales permitidos son `=`, `!=`, `<`, `>`, `<=`, `>=` y se pueden encadenar condiciones con las operaciones lógicas *and* (`&&`) y *or* (`||`).

### Bucles con `while`
La instrucción iterativa con `while` tiene la semántica habitual.

Ejemplo: `while a > 0 { a <- a / 2 }`.

Como se ha dicho antes, los operadores relacionales permitidos son `=`, `!=`, `<`, `>`, `<=`, `>=` y se pueden encadenar condiciones con las operaciones lógicas *and* (`&&`) y *or* (`||`).

### Invocación de función

La llamada a una función tiene la semántica habitual.
Si el número de los parámetros pasado no coinciden a los declarados saltará un error. La sintaxis es sin paréntesis ni comas.

Ejemplo: `Suma x + y 2`.

Si se llama a una función que no ha sido declarada saltará un error.

### Expresiones
Los operadores aritméticos son los habituales (`+`, `-`, `*`, `/`, `%) y con la misma prioridad que en C. Evidentemente, se pueden usar paréntesis. Todos los operadores aritméticos son de enteros.

Los operadores relacionales (`=`, `!=`, `<`, `>`, `<=`, `>=`) devuelven cero para el falso y uno para el cierto.

Si una variable no ha estado inicializada, saltará un error.

# Uso de Funx

Para usar el lenguaje Funx se tiene una página web donde se puede dar programas en Funx y te devuelve la salida del programa. 

La página web tiene 4 apartados:
- Funciones: Este apartado guardará una lista de las funciones que están declaradas.
- Variables: Este apartado guardará una lista de las variables que están declaradas.
- Consola: Aquí es donde escribimos nuestro programa escrito en Funx, nuestro input.
- Resultados: Este apartado enseñará las últimas cinco entradas y sus respectivos resultados.

