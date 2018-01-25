# Problema 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

## Solução
Mais um problema simples que tem uma solução simples. Podemos usar as mesmas funções next_prime and is_prime do problema 3 neste problema e executar um loop de 1-10001 para buscar o primo que queremos. O pseudo-código é:

```
p=2
para i=0 até 10001 faça
    p = next_prime(p)
fim
```

No meu mac, esse código leva 0.230s para executar. Existem maneiras melhores de procurar por números primos, mas por hora essa implementação está ok.

# Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

## Solution
One more simple problem that has a simple solution. We can use the same *next_prime* and *is_prime* functions of problem 3 in this problem and loop from 1 to 10001 to find the primes we want. The pseudocode is:

```
p=2
for i=0 to 10001 do
    p = next_prime(p)
end
```

No meu mac, esse código leva 0.230s para executar.
