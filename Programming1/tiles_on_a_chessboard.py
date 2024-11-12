import sys


def count_tiles(tile_size, chessboard):
    tiles = 0
    for row in chessboard:
        cons = 0

        for i in row:
            if i == 0:
                cons += 1
            if i != 0:
                cons = 0
            if (cons - tile_size) + 1 > 0:
                tiles += 1
    return tiles


tile_size = int(input())

n = 0
while True:

    chess_board_size = int(input())
    if chess_board_size == 0:
        break

    board = []

    for i in range(chess_board_size):
        row = []
        # build a row of the matrix
        for word in input().split():
            row.append(int(word))
        board.append(row)

    columns = []

    for i in range(chess_board_size):
        columns.append([sub[i] for sub in board])

    print(count_tiles(tile_size, board) + count_tiles(tile_size, columns))
