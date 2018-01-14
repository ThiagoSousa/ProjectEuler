# Problema 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

## Solução
Assim como o Problema 1, esse é um problema bem simples de se resolver, na verdade. Temos que somar os números pares da sequência de Fibonacci que não excedem 4 milhões. A solução mais trivial e que funciona rápido é calcular a sequência de fibonnaci um por um até que o número não exceda 4 milhões.

O pseudo-código mostra o algoritmo implementado e como o problema foi resolvido. As variáveis *a* e *b* contém os dois primeiros números da sequência e *b* vai sempre receber o próximo número ao somar *a+b*, e a receber o valor antigo de *b*.
```
a = 1
b = 2
sum = 2
while(b<4000000){
    aux = b
    b = a+b
    b = a
    if (b mod 2 == 0) sum += b
}
```

Quantos números passamos nessa iteração? Como a sequência cresce rápido, em apenas 31 iterações *b* passa a valer 4613732, o que já é maior que o máximo da sequência que queremos achar.

Não vou colocar  o resultado final aqui, mas vai estar no vídeo.

# Problem 1
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

## Solution
As problem 1, this is a very simple problem to solve. We have to sum all even fibonacci numbers that is not bigger than 4 million. The most trivial solution is to calculate the fibonacci sequence one by one until we reach our maximum desired value.

The pseudo-code show the implemented algorithm. The vars *a* and *b* receive the first two values of the sequence and at each iteration, b receives the next value of the sequence *b=a+b* and *b* receives the previous value of *a*
```
a = 1
b = 2
sum = 2
while(b<4000000){
    aux = b
    b = a+b
    b = a
    if (b mod 2 == 0) sum += b
}
```

How many numbers have we iterated? The sequence grows fast, in only 31 iterations, the value of *b* is 4613732, which is already our maximum.


I am not going to place the result here but, it will be in the video.
