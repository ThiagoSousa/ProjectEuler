# Problema 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

## Solução
O problema pede para encontrar qual é o número triangular que tem mais de 500 divisores. Primeiramente, essa sequência de números triangulares é uma sequência na qual sempre vamos adicionando o número da posição. Achar a soma dessa sequência é muito trivial. Porém, não é isso que queremos. Precisamos achar quantos divisores os números da sequência tem. A maneira mais simples para resolver é iterar sobre a sequência e calcular quantos divisores cada número tem, até achar o número que tem mais de 500 divisores.

A maneira de resolver esse problema de forma rápida é achar uma função que calcule o número de divisores de um número *n* de forma rápida. A maneira mais trivial é fazer um loop procurando números menores que o número em questão que sejam divisíveis por *n*. Precisamos verificar todos os números de *1->n*? Não, porquê:

* Sabemos que todos os números são divisíveis por 1 e por eles mesmo.
* Sabemos que o maior dos divisores é *n/2*, então teoricamente só precisamos ir até *n/2*.
* Sabemos também que os divisores vem em pares. Por exemplo: dividir 100/2 resulta em 50. Logo sabemos que 2 e 50 são divisores de 100. Assim, não precisamos ir até *n/2* e sim até a raiz quadrada de *n*, pois todos os pares de divisores estarão incluídos nesse intervalo.

Portanto, podemos fazer uma função que calcula o número de divisores de n, em complexidade de tempo $O(sqrt(n))$.

```
função cont_divisores(n):
    se n==1 retorna 1
    cont = 0
    para i=2 até raiz(n) faça
        se (n mod i ==0) cont +=2
    fim
    
    retorna cont+2
fim
```

Enfim, a função é rápida para resolver este problema. Há maneiras mais rápidas, mas esta deve dar para resolver. Continuando, agora, só precisamos gerar os números da sequência de números triangulares e testar o número de divisores de cada número. Um simples loop basta:

```
n = 1
i = 1
enquanto (cont_divisores(n)<=500) faça
    i++
    n = n+i
fim
```

Este código roda em 4.307s no meu mac.


# Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
## Solution
The problem asks to find which triangular number has more than 500 divisors. First, this sequence of triangular numbers is a sequence in which we are always adding the position of the number 1+2+3+4, ... . Finding the sum of this sequence is very trivial. But that is not what we want. We need to find how many divisors the sequence numbers have. The simplest way to solve is to iterate over the sequence and calculate how many divisors each number has, until you find the number that has more than 500 divisors.

The way to solve this problem quickly is to find a function that calculates the number of divisors of a number *n*. The most trivial way is to loop for numbers smaller than the number in question that are divisible by *n*. Do we need to check all * 1->n * numbers? No, these are the reasons:

* We know that all numbers are divisible by 1 and by themselves.
* We know that the largest of the divisors is *n/2*, so theoretically we just need to go up to *n/2*.
* We also know that divisors come in pairs. For example, dividing 100/2 results in 50. We now know that 2 and 50 are divisors of 100. Thus, we do not have to go up to *n/2 * but to the square root of *n*, since all pairs of divisors included in this range.

Therefore, we can create a function that calculates the number of divisors of n, in time complexity $O(sqrt(n))$.

````
function cont_divisors(n):
    if n==1 return 1
    cont = 0
    for i=2 até sqrt(n) do
        if (n mod i ==0) cont +=2
    end
    return cont+2
end
````

The function is fast to solve this problem. There are faster ways, but this one must be able to solve it quickly. Moving on, we  need to generate the numbers of the sequence of triangular numbers and test the number of divisors of each number. A simple loop is enough to pass through them:

```
n = 1
i = 1
while (cont_divisors(n)<=500) do
    i++
    n = n+i
end
```

This code runs in 4.307s in my machine. 
