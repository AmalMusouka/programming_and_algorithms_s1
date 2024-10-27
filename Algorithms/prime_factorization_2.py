import math

initial_num = int(input())
num = initial_num
divisors = []
prime_factors = ""
upper_limit = math.isqrt(num)
i = 2
factors = []
non_primes = []


while i <= upper_limit:
    if num % i == 0:
        num = num // i
        divisors.append(i)
        factors.append(num)
    else:
        i += 1

for factor in factors:
    for divisor in divisors:
        if factor % divisor == 0:
            if factors.count(factor) > 0 and factor != divisor:
                non_primes.append(factor)
                break


primes = [x for x in factors if x not in non_primes and x != 1]
check = all(numbers in divisors for numbers in primes)


for i in range(0, len(divisors)):
    for prime in primes:
        if i >= 1 and divisors[i] == divisors[i - 1]:
            pass
        elif len(divisors) == len(factors) == 1:
            prime_factors = str(divisors[0]) + " * " + str(factors[0])
        else:
            if divisors.count(divisors[i]) > 1:
                if i == 0:
                    prime_factors = (
                        prime_factors
                        + str(divisors[i])
                        + "^"
                        + str(divisors.count(divisors[i]))
                    )
                else:
                    prime_factors = (
                        prime_factors
                        + " * "
                        + str(divisors[i])
                        + "^"
                        + str(divisors.count(divisors[i]))
                    )
            else:
                if i == 0:
                    prime_factors = prime_factors + str(divisors[i])
                else:
                    prime_factors = prime_factors + " * " + str(divisors[i])

if check == False:
    for prime in primes:
        if str(prime) not in prime_factors:
            prime_factors = prime_factors + " * " + str(prime)

if divisors == []:
    prime_factors = initial_num


print(prime_factors)
