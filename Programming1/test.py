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

# divisors = [2, 3, 5, 7, 11]
# factors = [10, 20, 30, 40, 25]
# non_primes = []

# for factor in factors:
#     for divisor in divisors:
#         if factor % divisor == 0:
#             if factors.count(factor) > 0:
#                 non_primes.append(factor)
#                 break

# primes = [x for x in factors if x not in non_primes]
# print(primes)


## Integer square root ##

# Write a program that reads an integer n>=0 and prints the square root of n
# (if it is an integer), otherwise 'Not a square'. Do not use any floating-point numbers.
# Your program should run in O(logn)


# def isqrt(n):
#     lo = 0
#     hi = n
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if mid * mid == n:
#             return mid
#         elif mid * mid < n:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return None


# project eulers problem 8
# finding the highest product of 13 digits in an n digit number

# product = 1
# product_len = 0
# zeros = 0
# highest = 0
# for i in range(len(digits)):
#     #Add a digit
#     product_len += 1
#     if digits[i] == 0:
#         zeros += 1
#     else:
#         product += digits[i]
#         #Remove a digit (maybe)
#     if product_len > 13:
#         product_len == 1
#         if digits[i-13] == 0:
#             zeros -= 1
#         else:
#             product //= digits[i - 13]
#         #Find new max
#             if product_len == 13 and zeros == 0 and product > highest:
#                 highest = product


# Project eulers problem 9

# for a in range(1, 1001):
#     for b in range(a, 1001):
#         c = 1000 - a - b
#         if a * a + b * b == c * c:
#             print(a, b, c, a * b * c)
#         elif a * a + b * b > c * c:
#             #much more efficient adding this
#             break

# import math


# def findPrime(n):
#     if n <= 2:
#         return []

#     isPrime = [True] * (n)
#     isPrime[0] = False
#     isPrime[1] = False

#     for i in range(2, math.isqrt(n) + 1):
#         if isPrime[i]:
#             for x in range(i * i, n, i):
#                 isPrime[x] = False

#     return [i for i in range(n) if isPrime[i]]


# print(findPrime(100))


# def find_peaks():
#     import sys

#     prev_height = None
#     curr_height = None
#     next_height = None
#     distance = 0
#     plateau_start = None

#     for line in sys.stdin:
#         height = float(line.strip())

#         if height < 0:
#             break  # End of input

#         if distance > 0:
#             prev_height = curr_height

#         curr_height = height

#         # Look ahead for the next height (next measurement)
#         if distance > 0:
#             next_line = sys.stdin.readline()
#             if next_line:
#                 next_height = float(next_line.strip())
#             else:
#                 next_height = None  # End of input

#         # Check for a peak
#         if prev_height is not None and next_height is not None:
#             if curr_height > prev_height and curr_height > next_height:
#                 # Found a peak
#                 print(f"distance {distance} height {curr_height:.1f}")
#             elif curr_height == prev_height and curr_height > next_height:
#                 # Found the end of a plateau
#                 plateau_start = distance - 1  # The start of the plateau
#             elif curr_height > prev_height and curr_height == next_height:
#                 # Found the start of a plateau
#                 plateau_start = distance

#         # Update for next iteration
#         distance += 1
#         if next_height is not None:
#             next_height = None  # Reset for the next round

#     # Check if we had a plateau
#     if plateau_start is not None:
#         print(f"distance {plateau_start} height {curr_height:.1f}")


# # Call the function when this script is executed
# if __name__ == "__main__":
#     find_peaks()


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
         return f'x= {self.x}, y= {self.y}'
        
    def distance_to(self, q):
            x = self.x - q.x
            y = self.y - q.y 
            return math.sqrt(x ** 2 + y ** 2)
    # Return the distance from this point
    # to the origin
        
    def from_origin(self):
        return self.distance_to(Point(0,0))
    
    def is_origin(self):
        return self.from_origin() == 0.0
    

    # a line segment between two points
    class Line:
         def __init__(self, p, q):
              self.p = p
              self.q = q

         def __refr__(self):
              return f'{self.p} - {self.q}'
         
    
         def length(self):
              return self.p.distance_to(self.q)
         

    class Vector:
        def __init__(self, *args):
            self.a = args

         # Return the number of dimensions of a vector.
        def dims(self):
            return len(self.a)
         
         # Return the length of a vector
        def length(self):
            s = 0
            for x in self.a:
                s += x * x
                return math.sqrt(s)
              
         # Dot product of vectors
        def dot(self, w):
            assert self.dims() == w.dims()
            s = 0
            for i in range(self.dims()):
                s += self.a[i] * w.a[i]
                return s
              
        def add(self, w):
            assert self.dims() == w.dims()
            b = []
            for i in range(self.dims()):
                b.append(self.a[i] + w.a[i])
            return Vector(*b)
        


    # Store a 24-hour time, eg: 15:36:02 or 11:18:25
    class Time:
        def __init__(self, h, m, s):
            self.n = 3600 * h + 60 * m + s

        # Add d seconds to self
        def add(self, d):
            x = (self.n + d) % (24 * 3600)
            t = Time(0, 0, 0)
            t.n = (self.n + d) % (24 * 3600)
            return t
        
        def __repr__(self):
            