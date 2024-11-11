import sys


# to check the rows
def check_rows(matrix):

    row_sum = []

    for row in matrix:
        row_sum.append(sum(row))

    output = []
    for x in row_sum:
        if x not in output:
            output.append(x)

    return output


# to check the columns
def check_columns(matrix):

    column_sum = []

    for column in range(len(m[0])):
        t = 0
        for row in m:
            t += row[column]
        column_sum.append(t)

    output = []
    for x in column_sum:
        if x not in output:
            output.append(x)

    return output


# check the diagonals
def check_diagonals(matrix):

    diagonal_sum_1 = 0
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if i == j:
                diagonal_sum_1 += matrix[i][j]

    diagonal_sum_2 = 0
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if i == (len(m[0]) - 1) - j:
                diagonal_sum_2 += matrix[i][j]
    return diagonal_sum_1, diagonal_sum_2


def findpos(matrix):

    zero = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == zero:
                return (i, j)


m = []
for line in sys.stdin:
    # build a row of the matrix

    row = []
    for word in line.split():
        row.append(int(word))

    m.append(row)
# find the difference between the sum of the row with 0 and the ones without
rowsums = check_rows(m)
diff = max(rowsums) - min(rowsums)
zero_pos = findpos(m)
zero_pos_row = list(zero_pos)[0]
zero_pos_column = list(zero_pos)[1]

# change the value of the 0 to the difference
m[zero_pos_row][zero_pos_column] = diff

# check if the square is magic
columns = set(check_columns(m))
rows = set(check_rows(m))
diag = set(check_diagonals(m))


if columns == rows == diag and diff != 0:
    Result = "\n".join([" ".join([str(c) for c in lst]) for lst in m])
    print(Result)

else:
    print("Can't be magic")
