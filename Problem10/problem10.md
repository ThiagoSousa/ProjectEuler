# Problema 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## Solução
Para este problema vou seguir a mesma solução de geração de primos dos problemas 3 e 7, nas quais usamos a função *next_prime*. Já expliquei a implementação desta função no problema 3. Neste caso, a solução mais simples é somar os próximos primos da sequência. Não há muito a explicar:

```
p=2
soma = 0
enquanto p<2000000 faça
    soma = soma + p
    p = next_prime(p)
fim
```

Este código roda em 14.10s na minha máquina. Tem maneiras melhores de gerar primos mais rápidos, mas, por enquanto vou ficar por aqui


# Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## Solution
For this problem I will follow the same solution for generating prime numbers for problems 3 and 7, in which we use the function *next_prime*. I already explained the implementation of this function in problem 3. In this case, the simplest solution is to add the next prime of the sequence. There is not much to explain:

```
p=2
sum = 0
while p<2000000 do
    sum = sum + p
    p = next_prime(p)
end
```
This code runs in 14.10 seconds in my machine. It is not the best implementation, but, for now I won't implement any better way to generate prime numbers.
