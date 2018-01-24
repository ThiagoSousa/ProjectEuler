# Problema 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Solução
Mais um problema simples, ainda não está complicado. E há duas maneiras de resolver esse problema. Por força bruta ou no papel. Vamos as duas formas.

### Força Bruta
A maneira mais simples é de executar um loop indo de 1-100 e calcular a soma dos quadrados e somar os números e elevar a soma ao quadrado. No fim, tirar a diferença. Eis o pseudocódigo dessa solução simples, onde variável *a* representa a soma dos quadrados e *b* representa o quadrado da soma.

```
a = 0
b = 0
para i=0 to 100 faça
    a = a+i*i
    b = b+i
fim
resultado = b*b-a
```

Essa solução roda em 0.038s no meu mac.

### Lápis e papel
Tem uma solução mais simples que essa usando sequência, parecido com o problema 1. Sabemos como somar uma sequência de números que tem um intervalo fixo, que é dado por Sn=(a1+an)*n/2. Este é o caso do "quadrado da soma":

S100 = (1+100)*100/2.

Podemos fazer o mesmo com a "soma dos quadrados", porém o cálculo é diferente. Neste caso, eu não sabia de nenhuma forma de cálcular a soma dos quadrados. Assim, fui pesquisar e [encontrei](https://brilliant.org/wiki/sum-of-n-n2-or-n3/) uma maneira de calcular a soma dos quadrados, que é dado por S^2n=n*(n+1)*(2n+1)/6. Assim podemos calcular a soma dos quadrados de 1 até 100.

S^2100 = 100*(100+1)*(2*100+1)/6

O resultado é dado por S100-S^2100.

# Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Solution
Once more, a simple problem, still not complicated. And there are two ways to solve this problem. By brute force or on the paper. Let's go both ways.

### Brute Force
The simplest way is to loop from 1-100 and calculate the sum of squares and, sum the numbers and calculate the square of the sum. In the end, subtract. Here is the pseudocode of this simple solution, where variable *a* represents the sum of squares and *b* represents the square of the sum.

```
a = 0
b = 0
for i=0 to 100 do
    a = a+i*i
    b = b+i
end
result = b*b-a
```

This solution executes in 0.038s in my computer.

### Pen and paper
It has a simpler solution than this using sequences, similar to problem 1. We know how to sum a sequence of numbers that has a fixed interval, which is given by Sn = (a1 + an)*n/2. This is the case of the "square of the sum":

S100 = (1+100)*100/2.

We can do the same with the "sum of squares", but the calculation is different. In this case, I did not know of any way to calculate the sum of the squares. So I researched and [found](https://brilliant.org/wiki/sum-of-n-n2-or-n3/) a way to calculate the sum of squares, which is given by S^2n = n*(n + 1)*(2n + 1)/6. Then, we can calculate the sum of squares from 1 to 100.

S^2100 = 100*(100+1)*(2*100+1)/6

The final result is given by S100-S^2100
