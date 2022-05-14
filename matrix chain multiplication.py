import sys


def matrixChainMultiplication(dims, i, j, T):
    if j <= i + 1:
        return 0


    min = sys.maxsize
    if T[i][j] == 0:
        for k in range(i + 1, j):
            cost = matrixChainMultiplication(dims, i, k, T)
            cost += matrixChainMultiplication(dims, k, j, T)
            cost += dims[i] * dims[k] * dims[j]
            if cost < min:
                min = cost


        T[i][j] = min


    return T[i][j]


if __name__ == '__main__':
    dims = [3,2,4,2,5]
    T = [[0 for x in range(len(dims))] for y in range(len(dims))]
    print("The minimum cost is", matrixChainMultiplication(dims, 0, len(dims) - 1, T))

input("press a button")s