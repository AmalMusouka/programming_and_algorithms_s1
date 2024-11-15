import sys


one = """cheetah
crocodile
hippo
kangaroo
lion
tiger
walrus
zebra"""


two = """List of animals:
elephant
giraffe
meercat
rhinoceros"""

three = ""


def merge(a, b, c):
    i = j = 0  # index into a, b

    for k in range(len(c)):
        if j == len(b):  # no more elements available from b
            c[k] = a[i]  # so we take a[i]
            i += 1
        elif i == len(a):  # no more elements available from a
            c[k] = b[j]  # so we take b[j]
            j += 1
        elif ord(a[i][0]) < ord(b[j][0]):
            c[k] = a[i]  # take a[i]
            i += 1
        else:
            c[k] = b[j]  # take b[j]
            j += 1


def merge_i(a, b, c):
    i = j = 0  # index into a, b

    for k in range(len(c)):
        if j == len(b):  # no more elements available from b
            c[k] = a[i]  # so we take a[i]
            i += 1
        elif i == len(a):  # no more elements available from a
            c[k] = b[j]  # so we take b[j]
            j += 1
        elif ord(a[i].lower()[0]) < ord(b[j].lower()[0]):
            c[k] = a[i]  # take a[i]
            i += 1
        else:
            c[k] = b[j]  # take b[j]
            j += 1


def merge_sort(a, b):
    if len(a) < 2:
        return
    c = [None] * (len(a) + len(b))

    merge(a, b, c)
    return c


def merge_sort_i(a, b):
    if len(a) < 2:
        return
    c = [None] * (len(a) + len(b))

    merge_i(a, b, c)
    return c


x = one.split("\n")
y = two.split("\n")
# print(merge_sort(x, y))
commands = sys.argv
if commands[1] == "-i":
    commands[4] = merge_sort_i(commands[2], commands[3])
else:
    commands[3] = merge_sort(commands[1], commands[2])


print(commands[3])
