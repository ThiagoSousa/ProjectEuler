# Problema 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

## Solução
Os problemas estão ficando um pouquinho mais trabalhosos, mas ainda estão simples de resolver. Neste problema temos que achar qual o número que tem a sequência mais longa de acordo com as regras acima.

Sabemos que para menos de 1 milhão, vai dar sempre 1 no fim, porém pode ter muitas iterações. E sabemos que é um problema de subproblemas. Supondo que *C(n)* é a sequência de *n*, então o tamanho desta sequência é *C(N/2)+1* se *n* é par ou *C(3n+1)+1* se n é impar. Desta forma, podemos resolver esse problema de suas formas diferentes: recursivamente ou iterativamente. Em ambos os casos, vamos guardar o tamanho da sequência para um valor *n* que encontrarmos, facilitando assim os cálculos. Além disso, começaremos de 1 milhão decrescendo até um, pois desta forma, vamos percorrer boa parte dos números no caminho e ir salvando as suas soluções.

### Iterativamente
A ideia é passar pelos números de 1 milhão -> 1 e, para cada número, ir gerando a sequência até chegar em um e contar quantos elementos a sequência de cada número tem. Vamos salvar essa contagem para um número *n* num hash, pois se alcançarmos um número que já está no hash é só retornar esse número +1, facilitando assim o cálculo. Desta forma, o pseudo-código é:

```
para i=1000000 até 1 faça
    n = i
    enquanto i>1 faça
        se n está na hash
            cont+= hash[n] + 1
        senão
            se n%2==0 n = n/2
            senão n = 3n+1
            cont++
        fim
    fim
    hash[i] = cont
    ordenar(hash)
fim
```

Este código roda em 10.8s em sua implementação em python.

### Recursivamente
A solução recursiva é basicamente a ideia do subproblema que eu expliquei antes, vamos chamar uma função chamada C(n) que se invoca recursivamente C(n/2) se n é par ou C(3n+1) se n é ímpar. A condição de parada da recursão é encontrar um número que já esteja na hash. Inicializamos a hash com um número 1, por exemplo.

```
hash[1] = 1
função C(n)
    se n não está na hash
        se n%2==0 hash[n] = C(n/2)+1
        senão hash[n] = C(3n+1)+1
    fim
    retorne hash
fim

para i=1000000 até 1 do C(i)
ordenar(hash)
```

Este código roda em 2.230s em sua implementação em python. Percebemos que a implementação recursiva é bem mais eficiente. A dinâmica de dividir para conquistar é bem eficiente para solução deste problema.


# Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

## Solution
The problems are taking a bit more work, but they are still simple to solve. In this problem we have to find the number with has the longest sequence, according to the rules of the Collatz sequence.

We know that for less than 1 million, it will always return 1 at the end, but it can have many iterations. And we know it's a problem with many subproblems. Assuming that *C(n)* is the sequence of *n*, then the size of this sequence is *C(n/2)+1* if *n* is even or *C(3n+1)+1* if *n* is odd. In this way, we can solve this problem in its different forms: recursively or iteratively. In both cases, let's save the size of the string to a *n* value we find, making calculations easier. In addition, we will start from 1 million decreasing to one, so in this way we will go through many of the numbers along the way and save their solutions.

### Iterative solution
The idea is to go through the numbers of 1 million -> 1 and, for each number, generate the sequence until you reach one and count how many elements the sequence of each number has. Let's save this count in a hash, so that if we reach a number that is already in the hash just return that number +1, thus facilitating the calculation. In this way, the pseudo-code is:

```
for i=1000000 to 1 do
    n = i
    while i>1 do
        if n is in hash
            cont += hash[n] + 1
        else
            if n%2==0 n = n/2
            else n = 3n+1
            cont++
        end
    end
    hash[i] = cont
    sort(hash)
end
```

This solution executes in 10.8s in its python implementation.

### Recursive solution
The recursive solution is basically the idea of the subproblem that I explained before, let's call a function called *C(n)* that recursively invokes *C(n/2)* if *n* is even or *C(3n+1)* if *n* is odd. The recursion stop condition is to find a number that is already in the hash. Initialize the hash with a number 1, for example.

```
hash[1] = 1
function C(n)
    if n is not in hash
        if n%2==0 hash[n] = C(n/2)+1
        else hash[n] = C(3n+1)+1
    end
    return hash
end

for i=1000000 to 1 do C(i)
sort(hash)
```

This code runs in 2.230s  in my mac, in its python implementation. We can actually see that the recursive solution works better than the iterative one. The idea of dividing to conquer is very efficient to solve this problem.
