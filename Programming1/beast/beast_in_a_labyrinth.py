# A beast is in a labyrinth, which is represented as a rectangular grid.
#
# At any moment, the beast is at one particular position and is turned in one of four possible directions (up, down, left and right).
#
# In each round the beast makes one move: it will either turn left, turn right or take one step forward.
#
# At the beginning, the beast will always have a wall to its right.
#
# As the beast moves it tries to follow this wall at all times (see the sample output below).
#
# Standard input will contain an integer N on its own line, followed by a map of the labyrinth.
#
# Individual characters depict individual positions: 'X' is a wall and '.' is an empty spot.
#
# The characters '^', '>', 'v' and '<' depict the beast turned upward, to the right, downward and to the left.
#
# The labyrinth will always be surrounded by walls.
#
# Your program should read the input and then move the beast N times.
#
# After each move, print a map of the labyrinth in the same form in which you read it. Write an empty line after each map.

import sys

class Labyrinth:
    def __init__(self, input_string: str):
        self.matrix = [list(line.strip()) for line in input_string.splitlines()]

    # row, column = find_beast()
    def find_beast(self):
        for y, row in enumerate(self.matrix):
            for x, column in enumerate(row):
                if column != 'X' and column != '.':
                    return y, x

    def is_wall(self, row, column):
        return self.matrix[row][column] == 'X'

    def is_empty(self, row, column):
        return self.matrix[row][column] == '.'


class Beast:
    def __init__(self, row, column, direction, labyrinth: Labyrinth, turned_right = False):
        self.column = column
        self.row = row
        self.direction = direction
        self.lab = labyrinth
        self.turned_right = turned_right

    def row_same_col_inc(self):
        return self.row, self.column + 1

    def row_inc_col_same(self):
        return self.row + 1, self.column

    def row_same_col_dec(self):
        return self.row, self.column - 1

    def row_dec_col_same(self):
        return self.row - 1, self.column

    # return the index of the position to the right of the beast to check whether it is empty or not
    def right_index(self):
        return {'>': self.row_inc_col_same,
                '^': self.row_same_col_inc,
                'v': self.row_same_col_dec,
                '<': self.row_dec_col_same}[self.direction]()

    # return the orientation of the beast depending on the current orientation and position to the right
    def right_state(self):
        return {'<': '^',
                '^': '>',
                '>': 'v',
                'v': '<'}[self.direction]

    # return the index of the position right in front of the beast to check whether it is empty or not
    def straight_index(self):
        return {'>': self.row_same_col_inc,
                '^': self.row_dec_col_same,
                'v': self.row_inc_col_same,
                '<': self.row_same_col_dec}[self.direction]()

    # return the orientation of the beast depending on the current orientation and position to the left
    def left_state(self):
            return {'<': 'v',
                    '^': '<',
                    '>': '^',
                    'v': '>'}[self.direction]

    #check the corresponding directions of the beast and decide where to move or rotate
    def check_surrounding(self):
        right_coordinates = self.right_index()
        straight_coordinates = self.straight_index()

        if self.lab.is_empty(right_coordinates[0], right_coordinates[1]) and not self.turned_right:
            self.turned_right = True
            return self.rotate_right()
        elif self.lab.is_empty(straight_coordinates[0],straight_coordinates[1]):
            self.turned_right = False
            return self.move_straight()
        else:
            self.turned_right = False
            return self.rotate_left()

    def move_n_times(self, n):
        for _ in range(n):
            self.check_surrounding()


    def print_as_str(self, matrix):
        result = ''
        for list in matrix:
            res = "".join(list)
            result += res + "\n"
        print(result)

    # change the orientation so that the beast is facing towards the right of its previous position
    def rotate_right(self):
        right_direction = self.right_state()
        self.lab.matrix[self.row][self.column] = right_direction
        self.direction = right_direction

        return self.print_as_str(self.lab.matrix)

    def move_straight(self):
        straight_coordinates = self.straight_index()
        self.lab.matrix[self.row][self.column] = "."
        self.lab.matrix[straight_coordinates[0]][straight_coordinates[1]] = self.direction
        self.row = straight_coordinates[0]
        self.column = straight_coordinates[1]

        return self.print_as_str(self.lab.matrix)

    # change the orientation so that the beast is facing towards the left of its previous position
    def rotate_left(self):
        left_direction = self.left_state()
        self.lab.matrix[self.row][self.column] = left_direction
        self.direction = left_direction

        return self.print_as_str(self.lab.matrix)

num_of_moves = int(input())
sample_input = ""
for line in sys.stdin:
    sample_input += line

lab = Labyrinth(sample_input)
beast_position = lab.find_beast()
beast = Beast(beast_position[0], beast_position[1], lab.matrix[beast_position[0]][beast_position[1]], lab)

beast.move_n_times(num_of_moves)
