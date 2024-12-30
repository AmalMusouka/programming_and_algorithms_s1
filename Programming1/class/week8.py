import math

class Vec:
    def __init__(self, *a): # *a takes any number of arguments into tuples
        self.a = a

    def __repr__(self):
        return 'V' + str(self.a)

    def length(self):
        sum = 0
        for x in self.a:
            sum += x ** 2
        return math.sqrt(sum)

    def __add__(self, w):
        b = []
        for i in range(len(self.a)):
            b.append(self.a[i] + w.queue[i])
        return Vec(*b)

    # scalar multiplication
    def __mul__(self, k):
        b = []
        for x in self.a:
            b.append(x * k)
        return Vec(*b)

    def __rmul__(self, z):
        return self * z


d = {'a': 1, 'b': 2, 'c': 3}
d['a'] += 1

print(d['a'] + 1)