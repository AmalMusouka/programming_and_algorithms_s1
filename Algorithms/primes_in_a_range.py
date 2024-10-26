import math

lower_limit = int(input())
upper_limit = int(input())
prime = []
prime_numbers = []


for i in range(lower_limit, upper_limit + 1):
    isPrime = False
    for j in range(2, math.isqrt(i) + 1):
        if i % j == 0:
            isPrime = True
    prime.append(isPrime)
    if isPrime == False:
        prime_numbers.append(i)

percentage = len(prime_numbers) / (upper_limit - lower_limit + 1) * 100

print("Number of primes: " + str(prime.count(False)))
if prime_numbers == []:
    print("Smallest prime: None")
    print("Largest prime: None")
else:
    print("Smallest prime: " + str(min(prime_numbers)))
    print("Largest prime: " + str(max(prime_numbers)))
print("Percentage of numbers that are prime: " f"{percentage:.1f}")
