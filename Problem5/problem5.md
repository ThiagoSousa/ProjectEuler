# Problema 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Solução
Ainda um problema bem simples de se resolver. Precisamos achar o menor número natural que é divisível por números de 1-20. A maneira mais simples é ir testando números até encontrar um que seja divisível por todos esses números. Como o pseudo-código mostra, a função *divisível_1_20(n)* verifica se o número é divisível pelos números de 1-20.

```
n=1
enquanto (!divisivel_1_20(n)) faça
    n++
fim
```

Porém, esse código pode ser melhorado, pois a função *divisivel_1_20* não precisa verificar a divisibilidade por todos os números de 1-20 e não precisamos ir de um e em um. Na verdade podemos eliminar algumas verificações de divisibilidade:

* 1: todos números são divisíveis por 1, não precisamos verificar isso.
* 2: para ser divisível por 4,6,8,10,12,14,16,18 e 20, precisa ser divisível por 2. Logo não precisamos verificar isso.
* 3: para ser divisível por 6,9,12,15,18, precisa ser divisível por 3. Logo, não precisamos verificar esse número também.
* 4: para ser divisível por 8,12,16 e 20, precisa ser divisível por 4. Logo, não precisamos verificar divisibilidade por 4.
* 5: idem para 10, 15 e 20.
* 6: idem para 12 e 18
* 7: idem para 14
* 8: idem para 16
* 9: idem para 18
* 10: idem para 20.
* 11-19: precisamos verificar se é divisível para números de 11-19.
* 20: também não precisamos verificar pois, podemos andar de 20 em 20.

Logo, a função *divisivel_1_20(n)* e o pseudo-código optimizado:

```
função divisivel_1_20(n)
    se (n mod 19!=0) ou (n mod 18!=0) ou (n mod 17!=0) ou (n mod 16!=0) ou (n mod 15!=0) ou (n mod 14!=0) ou (n mod 13!=0) ou (n mod 12!=0) ou (n mod 11!=0) faça
        retorne falso
    fim
    retorne verdadeiro
fim

n=1
    enquanto (!divisivel_1_20(n)) do
    n = n+20
fim
```

Roda em 2.912s no meu mac. Não vou postar o resultado aqui, mas estará no vídeo.

# Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Solution
Still a simple problem to solve. We need to find the smallest natural number that is divisible by numbers 1-20. The simplest way is to test numbers until you find one that is divisible by all these numbers. As the pseudo-code shows, the *divisible_1_20(n)* function checks whether the number is divisible by the numbers 1-20.

```
n=1
while (!divisible_1_20(n)) do
    n++
end
```

However, this code can be improved because the * divisible_1_20 * function does not need to check the divisibility f all numbers from 1-20 and we do not have to step one by one. In fact, we can eliminate some divisibility checks:

* 1: All numbers are divisible by 1, we do not need to check this.
* 2: To be divisible by 4,6,8,10,12,14,16,18 and 20, it must be divisible by 2. So we do not need to check this.
* 3: to be divisible by 6,9,12,15,18, a number must be divisible by 3. Therefore, we do not need to check this number either.
* 4: to be divisible by 8,12,16 and 20, it must be divisible by 4. Therefore, we also do not need to check divisibility by 4.
* 5: idem for 10, 15 and 20.
* 6: idem for 12 and 18
* 7: idem for 14
* 8: idem to 16
* 9: idem to 18
* 10: idem to 20.
* 11-19: we need to check if it is divisible for numbers from 11-19.
* 20: we also do not need to check, we can walk 20 by 20.

Therefore, the *divisible_1_20(n) * function and the optimized pseudo-code:

```
function divisivel_1_20(n)
    if (n mod 19!=0) or (n mod 18!=0) or (n mod 17!=0) or (n mod 16!=0) or (n mod 15!=0) or (n mod 14!=0) or (n mod 13!=0) or (n mod 12!=0) or (n mod 11!=0) do
        return false
    fim
    return true
end

n=1
while (!divisivel_1_20(n)) do
    n = n+20
end
```

It runs in 2.912s in my personal computer. I am not going to place the result here but, it will be in the video.

