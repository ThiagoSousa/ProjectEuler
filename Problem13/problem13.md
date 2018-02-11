# Problema 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

## Solução
Este problema é simples e tem duas maneiras de resolver em python (que é a linguagem que estou usando para estes problemas).

### Solução supersimples
Na verdade python já tem um modo de representação de números grandes (bigint) embutido na linguagem. Então uma maneira simples de resolver o problema é colocar todos esses números do problema num vetor e simplismente somar cada um. No fim, pegar somente os 10 primeiros dígitos. Nem pretendo colocar um pseudo-código aqui, mas a implementação em python leva
0.044s para resolver o problema.

### Solução um pouco mais elaborada
Acho que a ideia do problema e nos fazer pensar em como tratar números grandes. Então vamos tratar o problema de uma outra forma, vamos implementar, nós mesmos, o tipo bigint., pois assim, quem está fazendo em outra linguagem pode ter ideia de como resolver.

Para isso, vamos fazer uma classe (ou um tipo abstrato) para representar um número muito grande. Desta forma, o número vai ser representado com um vetor e teremos que fazer uma função para adicionar dois números. Vamos simplismente adicionar digito por dígito neste loop e se passar de 9, temos um resto que deve ser adicionado ao dígito seguinte. Obviamente, fazemos isso da direita para esquerda.

```
classe bigint(n):
    atributo numero = []
    
    função add(n)
        se tamanho(numero)>=tamanho(n) n = colocarzeros(n,tamanho(numero)-tamanho(n))
        senão colocarzeros(numero,tamanho(n)-tamanho(numero))
        resto = 0
        para i=tamanho(numero) até 0 faça
            numero[i] = numero[i]+n[i]+resto
            resto[i] = numero[i]/10
            numero[i] = numero[i] mod 10
        fim
        numero = [resto] + numero
    fim
fim
```

Assim, essa função add pode ser chamada para calcular a adição de todos os números da lista e no fim pegar os 10 primeiros.

```
n_objeto = new bigint(numeros[0])
para i=1 até 100 faça
    n_objeto(new bigint(numeros[i]))
fim
resultado = n_objeto.numeros[0..10]
```

Este código roda em 0.045s no meu mac.


# Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

## Solution
This problem is simple and has two ways to solve in python (the language I am using for solving project euler problems).

### Very simple solution
In fact, python already has a large number representation (bigint) embedded in the language. So a simple way to solve the problem is to put all these numbers into one vector and simply add up to each one. At the end, pick up only the first 10 digits. I do not even want to put a pseudo-code here, but the implementation in python takes 0.044s to solve the problem.

### A slightly more elaborate solution
I think the idea of ​​the problem is make us think about how to handle large numbers. So let's treat the problem in a different way, let's implement the bigint type ourselves, so that whoever is doing it in another language may have an idea of ​​how to solve it.

For this, let's make a class (or an abstract type) to represent a very large number. In this way, the number will be represented as an array and we will have to create a function to add two numbers. We will simply add digit per digit in this loop and if we pass over 9, we will have a remainder that must be added to the next digit. Obviously, we do this from right to left.

```
class bigint(n):
    attribute number = []

    function add(n)
        if tamanho(numero)>=tamanho(n) n = colocarzeros(n,tamanho(numero)-tamanho(n))
        else colocarzeros(numero,tamanho(n)-tamanho(numero))
        remainder = 0
        for i=tamanho(numero) to 0 do
            number[i] = number[i]+n[i]+remainder
            remainder[i] = number[i]/10
            number[i] = number[i] mod 10
        end
        number = [remainder] + number
    fim
fim
```

Thus, this add function can be called to calculate the addition of all the numbers in the list and in the end pick the top 10.

```
n_object = new bigint(numbers[0])
for i=1 to 100 do
    n_object(new bigint(numbers[i]))
fim
result = n_object.numbers[0..10]
```

This code runs in 0.045s  in my mac. 
