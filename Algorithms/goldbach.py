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
