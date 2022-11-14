"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""

matrix_1 = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

def search_in_matrix(matrix, target):
    ptr_row = 0
    ptr_col = len(matrix[0]) - 1
    while ptr_row > -1 and ptr_col > -1 and ptr_row < len(matrix) and ptr_col < len(matrix[0]):
        if target > matrix[ptr_row][ptr_col]:
            ptr_row += 1
        elif target < matrix[ptr_row][ptr_col]:
            ptr_col -= 1
        else:
            return [ptr_row, ptr_col]

    return [-1, -1]


search_in_matrix(matrix_1, 44)