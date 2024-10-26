# def bar(a):
#     for i in range(len(a)):
#         a[i] += 1
#         a = a[:]
# def foo(a):
#     for b in a + a[:]:
#         bar(b)
#         bar(b[:])

# m = [[1,2],[3,4]]
# foo(m)
# print(m)

from math import sqrt

n = int(input("Enter n: "))

i = 2
s = ""
while i <= int(sqrt(n)):
    if n % i == 0:  # n is divisible by i
        s += str(i) + " * "
        n = n // i
    else:
        i += 1

s += str(n)  # append the last factor
print(s)
