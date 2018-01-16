# Problema 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Solução
Este problema 3 ainda é simples, mas daqui a pouco começa a ficar complicado. Ele pede para encontrar o maior palíndromo que é um resultado de um produto de dois números de 3 dígitos. Palíndromos são números (ou palavras) que se lê da mesma forma da direita para a esquerda ou vice-versa. Por exemplo, o número que eles nos deram: 9009.

Podemos resolver na força bruta, pois apenas precisamos testar números entre 100-999 que são de 3 dígitos. Assim podemos fazer dois loops aninhados para calcular a multiplicação entre esses dois números. Assim sendo, verificamos se é o maior até então e se é palíndromo. O pseudocódigo abaixo mostra como fazer:

```
max = 0
para i=100 até 999 faça
    para j=100 até 999 faça
        numero = i*j
        se número>max e épalindromo(número) max = número
    end
fim
```

Mas, como verificar se é um palíndromo? Podemos comparar se os dígitos são iguais no começo e no fim e vamos nos movendo em direção ao centro. Se encontramos um dígitos diferentes, não é palindromo, se nos encontramos no centro, então é. Por exemplo: 90122109, que tem 8 dígitos. Comparamos assim as posições (começando de zero, sempre):

* 0-7
* 1-6
* 2-5
* 3-4 (é palíndromo)

Já o número 9019, que tem 4 dígitos, comparamos as posições 0-3, mas verificamos dígitos diferentes em 0-1. Logo, não é palíndromo. Assim sendo, abaixo está a função para o palíndromo. A função *tamanho* é genérica para calcular o número de dígitos de *n*. Para fins de otimização deste código é importante verificar se *número>max* antes da função de verificação de palíndromo na condicional do pseudocódigo anterior, pois auxilia num curto circuito.

```
função épalíndromo(n):
    para i=0 até tamanho(n) faça
        se n[i]!=n[tamanho(n)-i] retorna falso
    fim
    retorna verdadeiro
fim
```
O código roda em 0.058s no meu mac. Não vou colocar o código aqui, mas vai estar no vídeo.

# Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Solution
This problem 3 is still simple, but it will soon start to get complicated. The problem queries us find the largest palindrome which is a result of a product of two 3-digit numbers. Palindromes are numbers (or words) that read the same way from right to left or vice versa. For example, the number they gave us: 9009.

We can solve on brute force because we just need to test numbers between 100-999 which are only 3 digits. So, we can make two nested loops to calculate the multiplication between these two numbers. Therefore, we verify if it is the largest until then and if it is palindrome. The pseudocode below shows how to do:

So, to solve the problem, we can do the same for the number in question. The pseudo-code would be as follows:

```
max = 0
for i=100 to 999 do
    for j=100 to 999 do
        number = i*j
        if number>max and ispalindrome(number) max = number
    end
end
```

But how to check if it is a palindrome? We can compare if the digits are equal at the beginning and at the end and we always move toward the center. If we find different digits, it is not palindrome, if we are in the center, then it is. For example: 90122109, which has 8 digits. So we compare the positions (starting from zero, always):

* 0-7
* 1-6
* 2-5
* 3-4 (it is palindrome)

Number 9019, which has 4 digits, positions 0-3 are ok, but we find different digits in 0-1; therefore, it is not palindrome. So, below is the function for the palindrome. The *size(n)* function is a generic one for calculating the number of digits of *n*. For optimization of this code it is important to check if *number>max* before the palindrome verification function in the conditional of the previous pseudocode, because it results in a slightly faster version of the algorithm

```
function ispalindromo(n):
    for i=0 to size(n) do
        if n[i]!=n[tamanho(n)-i] return false
    end
    return true
end
```

It runs in 0.058s in my personal computer. I am not going to place the result here but, it will be in the video.

