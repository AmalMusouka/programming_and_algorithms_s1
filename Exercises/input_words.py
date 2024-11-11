import sys

count = 0

for line in sys.stdin.readlines():
    count += len(line.split())


print(count)
