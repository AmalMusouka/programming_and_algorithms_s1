import sys

length = 0

for line in sys.stdin.readlines():
    for each in line.split():
        if length < len(each):
            length = len(each)
            longest = each

print(longest)
