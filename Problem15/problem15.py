######################################################################################################
### Problem 15: How many such routes are there through a 20x20 grid?
### Autor: Thiago de Sousa Silveira
######################################################################################################

def L(i,j):
    #if matrix[i][j]>0:
    #    return matrix[i][j]
    l = 0
    if i>0:
        l += L(i-1,j)
    if j>0:
        l += L(i,j-1)
    if i==0 and j==0:
        l+=1
    #matrix[i][j] = l
    return l

#matrix = [[] for i in range(21)]
#for i in range(21):
#    matrix[i] = [0 for j in range(21)]

print L(20,20)
