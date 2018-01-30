# Problema 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

## Solução
Ainda estamos nos problemas simples . Problema 9 pede para encontrarmos o produto dos lados do triângulo retângulo cujo perímetro dá 1000. Bom, consegui pensar em duas soluções para este problema. Vamos a elas:

### Força Bruta
A primeira ideia consiste em testar valores de a e b de 0-999, inferir o valor de c e testar se a solução é válida, isto é, se c>b e c=raiz(a*a+b*b).

```
para a=0 até 999 faça
    para b=a+1 até 999 faça
        c = 1000-a-b
        se c>b e c == raiz(a*a+b*b) então resultado = a*b*c
    fim
fim
```

No meu mac, esse código leva 0.143s para executar.

### Inferindo o valor de *b* e *c*
Esta solução é diferente da primeira no ponto de que somente vamos procurar os valores de um lado e inferir os outros dois. Para isso vamos fazer uma manipulação matemática.

Sabemos que $a+b+c=1000$ e $a^2+b^2=c^2$ -> $sqrt(a^2+b^2) = c$. Assim, podemos substituir c na equação do perímetro e depois isolar b, assim pode ser inferido a partir de a. Substituindo então temos:

$a+b+sqrt(a^2+b^2) =1000$
$sqrt(a^2+b^2) =1000-a-b$
$a^2+b^2 =(1000-a-b)^2$
$a^2+b^2 =(1000-a-b)*(1000-a-b)$
$a^2+b^2 =1000000-1000a-1000b-1000a+a^2+ab-1000b+ab+b^2$
$0 =1000000-2000a-2000b+2ab$
$1000000-2000a =b(-2000+2a)$
$b=\frac{1000000-2000a}{-2000+2a}$

Assim, com c e b sendo inferido, podemos escrever um pseudocódigo com somente um loop:

```
para a=0 até 999 faça
    b = (-1000000+2000*a)/(-2000+2*a)
    c = 1000-a-b
    se b>0 e b>c e c==raiz(a*a+b*b) resultado = a*b*c
fim
```

Este código roda em 0.038s segundos na minha máquina. É menos que a versão anterior, mas como são poucos valores a se iterar, não faz muita diferença.


# Problem 8
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

## Solution
We are still dealing with simple problems. Problem 9 asks to find the product of the sides of the right triangle whose perimeter gives 1000. Well, I could think of two solutions to this problem. Let's go to them:

### Brute force
The first idea is to test values of a and b from 0-999, infer the value of c and test whether the solution is valid, that is, if c> b and c = sqrt(a*a+b*b).

```
for a=0 to 999 do
    for b=a+1 to 999 do
        c = 1000-a-b
        if c>b and c == sqrt(a*a+b*b) result = a*b*c
    end
end
```

In my setup, it takes about 0.230s to execute.

### Inferring the value of two sides of the triangle
This solution is different from the first one, we will only look up the values on one side of the triangule and infer the other two. For solving it, we will do a mathematical manipulation.

We know that $ a + b + c = 1000 $ and $ a^2 + b^2 = c^2 $ - ^ sqrt (a^2 + b^2) = c $. Thus, we can replace c in the perimeter equation and then isolate b, so it can be inferred from a. Substituting then we have:

$a+b+sqrt(a^2+b^2) =1000$
$sqrt(a^2+b^2) =1000-a-b$
$a^2+b^2 =(1000-a-b)^2$
$a^2+b^2 =(1000-a-b)*(1000-a-b)$
$a^2+b^2 =1000000-1000a-1000b-1000a+a^2+ab-1000b+ab+b^2$
$0 =1000000-2000a-2000b+2ab$
$1000000-2000a =b(-2000+2a)$
$b=\frac{1000000-2000a}{-2000+2a}$

Thus, with c and b being inferred, we can write a pseudocode with only one loop:

```
for a=0 to 999 faça
    b = (-1000000+2000*a)/(-2000+2*a)
    c = 1000-a-b
    if b>0 and b>c and c==sqrt(a*a+b*b) result = a*b*c
end
```

This code runs in 0.038 seconds in my machine. It takes less than the previous version, but since there are few values to iterate, it does not make much difference.
