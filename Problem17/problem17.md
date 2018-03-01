# Problema 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

## Solução
Esse problema é fácil de resolver mas é uma tremenda dor de cabeça, pois cada pequeno detalhe faz toda a diferença. O problema nos pede para calcular quantas letras tem os números 1-1000 quando escritos por extenso, seguindo os nomes na lingua inglesa, como nos exemplos dados. De 1-9 temos nomes que serão reutilizados: "one", "two", ... , "nine". Também de 20-100: "twenty", "thirty", ... , "hundred", "thousand". Assim, podemos fazer um hash armazenar esses valores e escrever um loop que percorre os números de 1-1000 e separa cada algarismo do número: centenas, dezenas e unidade. Assim, podemos escrever a quantidade de cada algarismo. Atenção para números de 11-20, pois eles são excessão. O pseudocódigo fica assim:

```
hash[1] = "one"
hash[2] = "two"
...
hash[19] = "nineteen"
hash_dezenas[2] = "twenty"
hash_dezenas[3] = "thirty"
...
hash_dezenas[9] = "ninety"
soma = 0
para i=1 até 999 faça
    centena = i/100
    unidade = i mod 100
    se centena>0 então
        soma = soma + tamanho(hash[centena]) + 7
        se unidade>0 então soma = soma + 3
    fim
    se unidade<20 e unidade>0 então soma = soma + tamanho(hash[unidade])
    senão unidade>0 então
        dezena = unidade/10
        unidade = unidade mod 10
        soma = soma + hash_dezenas[dezena]
        se unidade>0 então soma = soma + tamanho(hash[unidade])
fim
soma = soma + tamanho("onethousand")
```

O código roda em 0.042s no meu computador pessoal


# Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

## Solution
This problem is easy to solve but it is a tremendous headache because every little detail makes all the difference. The problem asks us to calculate how many letters have the numbers 1-1000 when written in length, following the names in the English language, as in the examples given. From 1-9 we have names that will be reused: "one", "two", ..., "nine". Also from 20-100: "twenty", "thirty", ..., "hundred", "thousand". Thus, we can have a hash store these values and write a loop that traverses the numbers from 1-1000 and separates each digit from the number: hundreds, tens and tens. Thus, we can write the quantity of each digit. Watch out for numbers from 11-20 as they are odd. The pseudocode looks like this:

```
hash[1] = "one"
hash[2] = "two"
...
hash[19] = "nineteen"
hash_tens[2] = "twenty"
hash_tens[3] = "thirty"
...
hash_tens[9] = "ninety"
sum = 0
for i=1 to 999 do
    hundreds = i/100
    unit = i mod 100
    if hundreds>0 then
        sum = sum + size(hash[hundreds]) + 7
        if unit>0 then sum = sum + 3
    end
    if unit<20 and unit>0 then sum = sum + size(hash[unit])
    else unit>0 then
        tens = unit/10
        unit = unit mod 10
        sum = sum + hash_tens[tens]
        if unit>0 then sum = sum + size(hash[unit])
    end
end
sum = sum + size("onethousand")
```
The code runs in 0.042s in my personal computer.
