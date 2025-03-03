from problem18.problem18 import solve_triangle_matrix


fin = open("problem67/0067_triangle.txt", "r")

matrix = fin.read().rstrip()
fin.close()

matrix = matrix.split("\n")
matrix = [[int(column) for column in row.split(" ")] for row in matrix]

print(solve_triangle_matrix(matrix))