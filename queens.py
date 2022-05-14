n = int(input("Enter the value of n: "))
board = []#chest board


def getBoard():#define board
    for i in range(n):
        nthList = []
        for j in range(n):
            nthList.append(0)
        board.append(nthList)


def printBoard():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("")


def isSafe(row, col):#is she safe?
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[j][col] == 1:
            return False

#northwest
    i = row - 1
    j = col - 1
    while (i >= 0 and j >= 0):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
#east
    i = row - 1
    j = col + 1
    while (i >= 0 and j < n):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
#southwest
    i = row + 1
    j = col - 1
    while (i < n and j >= 0):
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1
#southeast
    i = row + 1
    j = col + 1
    while (i < n and j < n):
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j + 1
    return True


def Put(n, count):#where to place?
    if count == n:
        return True
    for i in range(n):
        for j in range(n):
            if isSafe(i, j):
                board[i][j] = 1#queen place
                count = count + 1
                if Put(n, count) == True:
                    return True
                board[i][j] = 0
                count = count - 1
    return False#time for run backward


getBoard()
Put(n, 0)
printBoard()

input("press a button")