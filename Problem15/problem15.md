# Problema 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

## Solução
Este problema é parecido com o problema anterior na maneira de que dá para elaborar uma solução usando a ideia de dividir para conquistar. Neste problema, temos que encontrar quantos caminhos diferentes existem de (0,0) até (20,20) considerando esse grid e que só se podemos andar na horizontal ou vertical. Vemos duas coisas importantes:

* cada pequena modificação num caminho é uma possibilidade diferente de um caminho.
* existem duas rotas que chegam até (20,20), que são por cima ou pela esquerda. Assim sendo, o problema de achar o número de rotas de (0,0) até (20,20) pode ser dividido no subproblema de achar o número de possibilidades até (19,20) e somar com o número de possibilidades até (20,19). O mesmo deve ser feito com esses dois subproblemas e assim por diante até chegarmos a (0,0).

Portanto, esse problema é característico de uma solução recursiva, onde o número de caminhos $L(x,y)= L(x-1,y)+L(x,y-1)$. Desta forma, podemos elaborar um pseudo-código de uma função recursiva, como mostrado abaixo. A condição de parada é quando os parâmetros são iguais a zero e também temos que prestar atenção para não contarmos posições negativas.

```
função L(i,j)
    l = 0
    se i>0 então l = l+L(i-1,j)
    se j>0 então l = l+L(i,j-1)
    se i==0 e j==0 então l++
    retornar l
fim
```

Este código, entretanto, leva muito tempo para executar. Por quê? O problema é o número gigantesco e repetitivo de chamadas de funções nesta recursão. Uma posição L(x,y) qualquer no meio grid é chamada diversas vezes na execução, e sua chamada carrega diversas outras chamadas recursivas, aumentando muito o tempo de execução. Podemos resolver isso salvando as soluções encontradas numa matrix por exemplo. Assim, evitando chamadas recursivas desnecessárias.
```
matrix[0..20][0..20] = -1
função L(i,j)
    se matrix[i][j] >= 0 então retorne matrix[i][j]
    l = 0
    se i>0 então l = l+L(i-1,j)
    se j>0 então l = l+L(i,j-1)
    se i==0 e j==0 então l++
    matrix[i][j] = l
    retornar l
fim
```

Este código roda em 0.051s no meu mac em sua implementação em python.


# Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

## Solution
This problem is similar to problem 14 in the way that we can divide to conquer it. In this problem, we have to find how many different paths there are from (0,0) to (20,20) considering this grid and that only if we can walk horizontally or vertically. We see two important things:

* every little change in a path is a different possibility of a path.
* There are two routes that arrive to (20,20), which are from above or from the left. Thus, the problem of finding the number of routes from (0, 0) to (20, 20) can be divided into the subproblem of finding the number of possibilities up to (19, 20) plus the number of possibilities up to (20, 19). The same must be done with these two subproblems and so on until we get to (0,0).

Therefore, this problem is characteristic of a recursive solution, where the number of paths $L (x, y) = L (x-1, y) + L (x, y-1)$. In this way, we can make a pseudo-code of a recursive function, as shown below. The stop condition is when the parameters are equal to zero and we also have to pay attention not to count negative positions.

```
function L(i,j)
    l = 0
    if i>0 then l = l+L(i-1,j)
    if j>0 then l = l+L(i,j-1)
    if i==0 and j==0 then l++
    return l
end
```

This code, however, takes a long time to execute. Why is that? The problem is the large and  repetitive number of function calls in this recursion. A position L (x, y) in the middle grid is called several times in the execution, and its call carries several other recursive calls, greatly increasing the execution time. We can solve this by saving the solutions found in a matrix for example. Thus, avoiding unnecessary recursive calls.

```
matrix[0..20][0..20] = -1
function L(i,j)
    if matrix[i][j] >= 0 then return matrix[i][j]
    l = 0
    if i>0 then l = l+L(i-1,j)
    if j>0 then l = l+L(i,j-1)
    if i==0 and j==0 then l++
    matrix[i][j] = l
    return l
end
```

This code runs in 0.051s,  in my mac, in its python implementation.
