# Problema 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

## Solução
É um problema bem simples para se resolver isso em Python, mas pode te dar uma dor de cabeça se voce estiver resolvendo esse problema numa linguagem sem suporte a BigInt. Precisamos somar os dígitos dos número que é $2^1000$, que é um número grande. Desta forma duas soluções são providenciadas.

### Solução simples
Python tem suporte nativo a BigInt, então facilita bastante calcular somente 2**1000. Desta forma o código fica como o pseudo-código abaixo. Este código leva 0.038s para executar em meu Mac.

```
numero = 2**1000
para i=0 até tamanho(numero)
    s = s + numero[i]
fim
```

### Solução mais complexa
Assim como no Problema 13, acho que a ideia do problema é nos fazer preocupar com BigInt, então vamos melhorar a classe que criamos no problema 13 para ter suporte a multiplicação de grandes inteiros. Assim, podemos fazer $2^1000$ através de 1000 multiplicações por 2, usando a classe big int.


Então temos que implementar uma multiplicação para BigInt. Como fazer isso? Essa é a parte da dor de cabeça, temos que fazer a multiplicação como fazemos no papel. Para cada dígito do segundo números, multiplicar por todos do primeiro, somar com o resto e se adicionar ao resultado final começando depois de um deslocamento. Assim como na adição,temos que começar da direita para a esquerda. Veja o pseudo código abaixo.

```
classe bigint(n):
    atributo numero = []

    função mult(n)
        resultado = new bigint("0")
        pos_i = 0
        para i=tamanho(numero) até 0 faça
            resto = 0
            pos_j = 0
            para j=tamanho(n) até 0 faça
               s = numero[i]*n.numero[j] + resultado[pos_i+pos_j] + resto
               resto = s/10
               resultado[pos_i+pos_j] mod 10
               pos_j++
            fim
            se resto>0 então resultado[pos_i+pos_j] = resto
            pos_i++
        fim
        inverter(resultado)
        numero = resultado
    fim
fim
```

O método de multiplicação tem dois loops aninhados para multiplicar cada dígito. As variáveis *pos_i*, *pos_j* controlam o dígito onde será escrito o resultado. Para executar podemos fazer um loop calculando a multiplicação de 2, 1000 vezes. Este código é um pouquinho mais lento que a implementação em Python e roda em 0.244s no meu Mac. Imagino que a implementação em Python seja bem mais eficiente e otimizada que esta implementação.


# Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

## Solution
It is a simple problem to solve this in Python, but it can give you a headache if you are solving this problem in a language that does not support BigInt. We need to sum the digits of the numbers which is $ 2^1000$, which is a large number. In this way two solutions are provided.

### Simple Solution
Python has native support for BigInt, so it makes it easy to calculate only 2**1000. The following pseudo-code below shows the implementation. This code takes 0.038s to run on my Mac.

```
number = 2**1000
for i=0 to size(numero)
    s = s + number[i]
end
```

### A little more complex solution
Just like in Problem 13, I think the idea of the problem is to make us worry about BigInt, so let's improve the class we created in Problem 13 to support the multiplication of large integers. Thus, we can make $ 2^1000$ through 1000 multiplications by 2, using the bigint class.

So we have to implement a multiplication for BigInt. How to do this? That is the part of the headache, we have to do multiplication as we do on paper. For each digit of the second numbers, multiply by all of the first, add with the rest and add to the final result starting after an offset. Just like in addition, we have to start from right to left. See the pseudo code below.

```
class bigint(n):
    attribute numero = []

    function mult(n)
        result = new bigint("0")
        pos_i = 0
        for i=size(numero) to 0 do
            remainder = 0
            pos_j = 0
            for j=size(n) to 0 do
                s = number[i]*n.number[j] + result[pos_i+pos_j] + remainder
                remainder = s/10
                result[pos_i+pos_j] mod 10
                pos_j++
            end
            if resto>0 then result[pos_i+pos_j] = remainder
            pos_i++
        end
        invert(result)
        number = result
    end
end
```

The multiplication method has two nested loops to multiply each digit. The variables *pos_i*, *pos_j* control the digit where the result will be written. In order to find the result, we can make a loop by calculating the multiplication of 2, 1000 times. This code is a bit slower than the Python implementation and runs at 0.244s on my Mac. I imagine the implementation in Python is much more efficient and optimized than this implementation.
