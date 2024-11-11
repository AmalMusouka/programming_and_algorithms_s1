import math


def solution_three(input_str: str, count):
    lines = input_str
    rules = [None] * count

    for line in lines:
        (clerk_from, clerk_to) = [int(num) - 1 for num in line]
        rules[clerk_from] = clerk_to

    total = []

    while True:
        rule_index = None
        links = 1

        # find the first non None rule
        for index in range(count):
            if rules[index] is not None:
                rule_index = index
                break

        if rule_index is None:
            break

        left = rule_index
        right = rules[rule_index]

        rules[left] = None

        while left != right:
            links += 1
            index_next = right
            right = rules[index_next]
            rules[index_next] = None

        total.append(links)

    return total


num = int(input())
val = []
for i in range(num):
    val.append([int(i) for i in (input()).split()])


cycles = solution_three(val, num)
lcm = 1
for i in cycles:
    lcm = math.lcm(lcm, i)

print(lcm)

#  How to prevent looking at the first Nones every single time
# result = 1
# for start in range(n):
#     if perm[start] is None:
#         continue
#     cycle = 1
#     ix, perm[start] = perm[start], None
#     while ix != start:
#         perm[ix], ix = None, perm[ix]
#         cycle += 1
#     result = math.lcm(result, cycle)
#
