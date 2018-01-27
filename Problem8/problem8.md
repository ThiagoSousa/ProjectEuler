# Problema 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?



## Solução
Um problema menos simples, mas que é fácil de resolver ainda. Neste caso temos que encontrar uma sequência de 13 números neste conjunto de números cuja multiplicação é a maior possível.

Minha ideia é testar cada possibilidade de 13 números. Assim um loop que vai de 0-986, calcula o produto dos treze números seguintes ao número da iteração. Portanto começando da posição *0*, eu multiplico todos os treze números seguintes: 7x3x1x6x7x1x7x6x5x3x1x3x3. Na iteração seguinte, eu começo da posição *1*: 3x1x6x7x1x7x6x5x3x1x3x3x0, e assim por diante. Segue o pseudocódigo, no qual eu tratei esse número de 1000 dígitos na variável número.



```
numero = "esse baita número acima"
função calcular_13(i)
    p = 1
    para j=i até i+13 faça
        p = p * numero[i]
    fim
fim

para i=0 até tamanho(numero)-13 faça
    p =calcular_13(i)
    se (p>max) max = p
fim
```

No meu mac, esse código leva 0.048s para executar.

# Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

## Solution
A less simple problem, but it is still easy to solve. My idea is to test every possibility of 13 numbers. So a loop ranging from 0-986, calculates the product of the thirteen numbers following the iteration number. So starting at position *0*, we multiply all of the following thirteen numbers: 7x3x1x6x7x1x7x6x5x3x1x3x3. In the following iteration, I start from position *1*: 3x1x6x7x1x7x6x5x3x1x3x3x0, and so on. Here is the pseudocode, in which I treated that 1000-digit number in the variable number.

```
number = ""
function calculate_13(i)
    p = 1
    for j=i to i+13 do
        p = p * number[i]
    end
end

for i=0 to size(number)-13 do
    p = calculate_13(i)
    if (p>max) max = p
fim
```

No meu mac, esse código leva 0.230s para executar.