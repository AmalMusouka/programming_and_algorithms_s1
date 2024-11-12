import math

x = input()
x = [int(i) for i in x.split()]


def findPrime(n):
    if n <= 2:
        return []

    isPrime = [True] * (n)
    isPrime[0] = isPrime[1] = False

    for i in range(2, math.isqrt(n) + 1):
        if isPrime[i]:
            for x in range(i * i, n, i):
                isPrime[x] = False

    return isPrime


def sumOfPrime(arr):
    primeSums = []

    primes = findPrime(max(arr) + 1)
    for i in range(0, len(arr)):
        if primes[arr[i]] and arr[i] < 5:
            primeSums.append(0)
        else:
            count = 0
            for first_prime in range(2, arr[i]):
                second_prime = arr[i] - first_prime
                if primes[second_prime] and primes[first_prime]:
                    count += 1
            if count % 2 == 0:
                primeSums.append(count // 2)
            else:
                primeSums.append(count // 2 + 1)

    goldbachPrimes = " ".join(str(x) for x in primeSums)

    return goldbachPrimes


print(sumOfPrime(x))


# def sieve(n):
#     if n < 2:
#         return [False,False]

#     prime = (n+1) * [True]
#     prime[0] = prime[1] = False
#     for i in range(2, math.isqrt(n) + 1):
#         if prime[i]:
#             for j in range(i * i, n + 1, i):
#                 prime[j] = False

#     return prime

# data = []
# for s in input().split():
#     data.append(int(s))

# is_prime = sieve(max(data))
# result = []
# for n in data:
#     count = 0
#     if n % 2 == 1:
#         if n > 2 and is_prime[n-2]:
#             count += 1
#     else:
#         for i in range(2, n // 2 + 1):
#             if is_prime[i] and is_prime[n-1]:
#                 count += 1
#     result.append(count)
# print(*result)
