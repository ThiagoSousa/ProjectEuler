def lattice_path(x: int, y: int) -> int:
    """
    Recursively calculates the number of lattice routes
    :param x: x coordinate
    :param y: y coordinate
    :return: number of routes
    """

    if x == 20 and y == 20:
        return 1

    result = 0
    if x < 20:
        result += lattice_path(x+1, y)
    if y < 20:
        result += lattice_path(x, y+1)

    return result


def lattice_path_dp(n: int = 2) -> int:
    """
    Dynamic programming to the lattice path solution. O(n^2)
    :param n: size of the grid
    :return: number of routes
    """

    matrix = [[0]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
    return matrix[n][n]

# print(lattice_path(0, 0))
print(lattice_path_dp(n=20))