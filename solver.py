import sys
import time

st = time.time()

def readFile(textfile):
    f = open(textfile, "r")
    next(f)
    i = 0
    j = 0
    matrix=[[0 for x in range(9)] for y in range(9)]

    while True:
        j = 0
        char=f.readline()
        for c in char:
            matrix[i][j] = int(c)
            j += 1
            if j == 9:
                i += 1
                break
        if i == 9:
            break
    return matrix

def checkSudoku(row, column, number, matrix_board):
    check = 0
    for i in range(0, 9):
        if matrix_board[row][i] == number:
            check = 1
    for i in range(0, 9):
        if matrix_board[i][column] == number:
            check = 1
    row -= row % 3
    column -= column % 3

    for i in range(0, 3):
        for j in range(0, 3):
            if matrix_board[row + i][column + j] == number:
                check = 1
    if check == 1:
        return False
    else:
        return True

class calls:
    numCalls = 0
c = calls()

def solveSudoku(matrix):
    c.numCalls += 1
    breakCon = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i][j] == 0:
                breakCon = 1
                row = i
                column = j
                break
    if breakCon == 0:
        print("Naive Backtracking Algorithm Solution: ")
        for i in matrix:
            print(i)
        print("Amount of Recursive Calls: ", c.numCalls)
        print("Execution Time: ", round(time.time() - st, 2), "seconds")
        exit(0)

    for i in range(0, 10):
        if checkSudoku(row, column, i, matrix):
            matrix[row][column] = i
            if solveSudoku(matrix):
                return True
            matrix[row][column] = 0
    return False

matrix = readFile(sys.argv[1])
solveSudoku(matrix)



