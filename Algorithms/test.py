import sys

previous = None
current = None
dist = 0
plateau_start = None


line = next(sys.stdin, "").strip()
if line and float(line) > 0:
    current = float(line)


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    next_measure = float(line)

    if next_measure < 0:
        break

    if previous is not None:
        if previous < current:
            if current > next_measure:
                print(f"distance {dist} height {current:.1f}")

    if previous is not None:
        if previous < current:
            if current == next_measure:
                plateau_start = dist
                while current == next_measure:
                    dist += 1
                    line = next(sys.stdin, "").strip()

                    if not line:
                        next_measure = None
                        break

                    next_measure = float(line)

                    if next_measure < 0:
                        break

                if next_measure is not None:
                    if next_measure < current:
                        print(f"distance {plateau_start} height {current:.1f}")

    previous = current
    current = next_measure
    dist += 1
