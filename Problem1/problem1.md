# Problema 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

## Solução
É um problema muito simples, na verdade, e há duas maneiras de resolver: pela força bruta e com papel e lápis mesmo calculando a soma das seqüências.

### Força Bruta
A solução usando força bruta é a abordagem mais simples. Consiste em iterar os números de 1 a 999 e somar aqueles que são múltiplos de 3 ou 5. Para checar quais são os múltiplos, simplesmente verifique quais números restam 0 ao dividir por 3 ou por 5.

* n ~ 1,2,3, ..., 999. Somar se o resto da divisão por 3 ou por 5 resulta em zero.

Pseudo-código:
```
for n=0 to 999 do
if (n mod 3==0) or (n mod 5==0) then
sum += n
endif
end
```

### Papel e lápis
O problema também pode ser resolvido usando sequências. Podemos somar todos os múltiplos de 3 e separadamente somar também todos os múltiplos de 5. E então, subtrair todos os números que são múltiplos de ambos 3 e 5. Neste caso, múltiplos de ambos 3 e 5, são múltiplos de 15 . Podemos listar esses números através das seqüências:

* **Múltiplos de 3:** 3, 6, 9, 12, 15, ..., 999
* **Múltiplos de 5:** 5, 10, 15, ..., 995
* **Múltiplos de 3 and 5 (Múltiplos de15)**: 15, 30, 45, ..., 990

Assim sendo, dado essas listas de números, podemos calcular a soma de cada sequência pela soma básica de uma sequência aritmética, dado pela equação Sn = (a1+an)*n/2, onde *n* é a quantidade de números na sequência.

* **s3** = ((3+999)*999/3)/2
* **s5** = ((5+995)*995/5)/2
* **s15** = ((15+990)*990/15)/2

O total é dado assim ao realizar o cálculo: s3+s5-s15

Não vou colocar  o resultado final aqui, mas vai estar no vídeo.

# Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

## Solution
It's a very simple problem and there are two main ways to solve it, by bruteforce and on pen and paper calculating the sum of the sequences.

### Bruteforce
The bruteforce and simplest approach is to iterate from 1 to 999 and sum the multiples of 3 or 5. To check the multiples simply check which numbers have mod 0 when divided by 3 or 5.

* n ~ 1,2,3, ..., 999. Sum if n mod 3==0 or n mod 5 ==0.

Here follows the pseudo-code:
```
for n=0 to 999 do
    if (n mod 3==0) or (n mod 5==0) then
        sum += n
    endif
end
```

### Pen and Paper
The problem can also be solved using sequences. We can sum up all multiples of 3 and  sum up all multiples of 5, separately. And then, subtract all numbers which are multiple of both 5 and 3. In this case, multiples of both 5 and 3, are basically multiples of 15.   We can list these numbers through the sequences:

* **multiples of 3:** 3, 6, 9, 12, 15, ..., 999
* **multiples of 5:** 5, 10, 15, ..., 995
* **multples of 3 and 5 (multiples of 15)**: 15, 30, 45, ..., 990

So, given this list, we can calculate the sum of each set of multiples separately using a basic sum of an arithmetic sequence, which is given by Sn = (a1+an)*n/2, where *n* here is the number of elements in the sequence.

* **s3** = ((3+999)*999/3)/2
* **s5** = ((5+995)*995/5)/2
* **s15** = ((15+990)*990/15)/2

So, the total is given by: s3+s5-s15

I am not going to place the result here but, it will be in the video.

