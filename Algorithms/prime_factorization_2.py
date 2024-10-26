import math

num = int(input())
divisors = []
prime_factors = ""
upper_limit = math.isqrt(num)
i = 2
factors = []


while i <= upper_limit:
    if num % i == 0:
        num = num // i
        divisors.append(i)
        factors.append(num)
    else:
        i += 1

if divisors == []:
    divisors.append(num)


for i in range(0, len(divisors)):
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
                    + " ^ "
                    + str(divisors.count(divisors[i]))
                )
            else:
                prime_factors = (
                    prime_factors
                    + " * "
                    + str(divisors[i])
                    + " ^ "
                    + str(divisors.count(divisors[i]))
                )

        else:
            if i == 0:
                prime_factors = prime_factors + str(divisors[i])
            else:
                prime_factors = prime_factors + " * " + str(divisors[i])


print(prime_factors)
print(divisors)
print(factors)
