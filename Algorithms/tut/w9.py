import random

# Suppose that we insert N values into a hash table with N buckets. What fraction of the buckets do we expect will be empty?
# Assume that N is a large number

def simulate_hashing(N):
    buckets = N * [0]
    for _ in range(N):
        buckets[random.randrange(N)] += 1
    return buckets


def my_abs(x):
    '''
    Compute the absolute value of any number
    '''
    return -x if x < 0 else x

# First to pass

def first(f, l):
    for i, x in enumerate(l):
        if f(x):
            return i
    return -1

def first_begin(ss, c):

    return first(lambda x: x != '' and x[0] == c, ss)

# bijection

def bijective(f, n):
    return set(map(f, range(n))) == set(range(n))

# bubble sort with key

# In the lecture we saw this bubble sort implementation with a key function f:

# Sort the list a, where we consider x to be greater than y
# if f(x) > f(y).
def sort_by(a, f):
    n = len(a)
    for i in range(n - 1, 0, -1):  # n - 1, ... 1
        for j in range(i):
            if f(a[j]) > f(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]

def sort_by_ans(a, f):
    n = len(a)
    f_a = list(map(f, a))
    for i in range(n - 1, 0, -1):  # n - 1, ... 1
        for j in range(i):
            if f_a[j] > f_a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                f_a[j], f_a[j + 1] = f_a[j + 1], f_a[j]
# This function will call f up to O(N2) times, where N is the length of a.
#  Rewrite the function so that it calls f only N times.
#  Hint: First generate a list of pairs; each pair will contain an element x from a, plus the value f(x).
