import sys

one = None
two = None
two_index = 1

is_plateau = None
plateau_index = None
index = -1

for line in sys.stdin:
    three = float(line)
    index += 1

    if three < 0:
        break

    if one is None:
        one = three
        continue

    if two is None:
        two = three
        continue

    if two == three:
        continue

    if two > one and two > three:
        print(f"distance {two_index}  height {two:.1f}")

    one = two

    two = three
    two_index = index
