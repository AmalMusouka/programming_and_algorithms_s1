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

divisors = [2, 3, 5, 7, 11]
factors = [10, 20, 30, 40, 25]
non_primes = []

for factor in factors:
    for divisor in divisors:
        if factor % divisor == 0:
            if factors.count(factor) > 0:
                non_primes.append(factor)
                break

primes = [x for x in factors if x not in non_primes]
print(primes)
