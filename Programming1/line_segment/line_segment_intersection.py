# The input of the program consists of 8 integers Ax, Ay, Bx, By, Cx, Cy, Dx, Dy that represent the coordinates of 4 points A, B, C, D in the Euclid plane.
#
# All numbers are on a single line, separated by spaces.
#
# The program should print ANO (Czech for yes), if the line segments AB and CD share at least one point; it should print NE (Czech for no) otherwise.
#
# As an example, for the input 0 0 1 1 0 1 1 0, the answer is ANO (yes).
import sys


def cross_product(a, b):
    cross = a[0] * b[1] - a[1] * b[0]
    if cross > 0:
        return 1
    elif cross < 0:
        return -1
    else:
        return 0

def check_overlapping(a, b, c, d):
    if ((a[0] <= c[0] <= b[0]) and (a[1] <= c[1] <= b[1])) or ((a[0] <= d[0] <= b[0]) and (
            a[1] <= d[1] <= b[1])):
        return True


def get_orientation(a, b, c, d):

    # make a the origin and then extend the rest accordingly
    if a == (0, 0):
        pass
    else:
        b = (b[0] - a[0], b[1] - a[1])
        c = (c[0] - a[0], c[1] - a[1])
        d = (c[0] - a[0], c[1] - a[1])

    orientation_1 = cross_product(b, d)
    orientation_2 = cross_product(b, c)

    #collinear
    if orientation_1 == orientation_2 == 0:
        check_overlapping(a, b, c, d)

    if orientation_1 == 0 and orientation_2 != 0:
        orientation_1 = -orientation_2
    elif orientation_2 == 0 and orientation_1 != 0:
        orientation_2 = -orientation_1

    return orientation_1, orientation_2


def num_from_input(input_string):
    list_of_numbers = []

    for number in input_string.split():
        list_of_numbers.append(int(number))

    return list_of_numbers

def check_orientation(to_point_a, to_point_b, from_point_a, from_point_b):

    if to_point_a != to_point_b and from_point_a != from_point_b:
        return True
    else:
        return False


def intersection(input_string):

    list_of_numbers = num_from_input(input_string)

    a = (list_of_numbers[0], list_of_numbers[1])
    b = (list_of_numbers[2] ,list_of_numbers[3])
    c = (list_of_numbers[4] ,list_of_numbers[5])
    d = (list_of_numbers[6] ,list_of_numbers[7])

    orientation_1 = get_orientation(a, b, c, d)
    orientation_2 = get_orientation(a, b, d, c)
    orientation_3 = get_orientation(c, d, a, b)
    orientation_4 = get_orientation(c, d, b, a)


    result = check_orientation(orientation_1, orientation_2, orientation_3, orientation_4)

    #checking if the orientations are all 0 to check for collinearity
    if (orientation_1 == orientation_2 == (0, 0)) or (orientation_3 == orientation_4 == (0, 0)):
        if check_overlapping(a, b, c, d) or check_overlapping(c, d, a, b):
            result = True


    if result is True:
        print("ANO")
    else:
        print("NE")




input_string = ""

for line in sys.stdin:
    input_string += line

intersection(input_string)




