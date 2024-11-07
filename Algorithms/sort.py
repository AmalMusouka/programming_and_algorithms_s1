import random


# given sorted arrays a and b, merge them into array c (merging) --> O(2N) == O(N)


def merge(a, b, c):
    assert len(a) + len(b) == len(c)

    i = j = 0
    for k in range(len(c)):
        if i == len(a):
            c[k] = b[j]
            j += 1
        elif j == len(b):
            c[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1


# MERGESORT - biggest con -> does not run in place


def mergesort(a):  # T(N) = O(N) + 2T(N/2) --> T(N) = O(NlogN)
    if len(a) < 2:
        return

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    mergesort(left)
    mergesort(right)
    merge(left, right, a)

    # QuickSort

    # Partition a[lo:hi] into two partitions a[lo:k] and a[k:hi], and return k.
    # Both partitions must be non empty!!


def partition(a, lo, hi):
    # Choose a pivot.
    p = a[random.randrange(lo + 1, hi)]

    i = lo
    j = hi - 1
    while True:
        # Advance i and j, looking for elements to swap.
        while a[i] < p:
            i += 1
        while a[i] > p:
            j -= 1

        # TRICKY
        if j <= i:
            return i

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


# recursive helper function
# Use quicksort to sort the values a[lo:hi]


def quick(a, lo, hi):
    if hi - lo < 2:
        return

    k = partition(a, lo, hi)
    quick(a, lo, k)
    quick(a, k, hi)


def quicksort(a):  # Worst case T(N) = O(N) + T(N-1) -> T(N) =O(N^2) disadvantage
    quick(a, 0, len(a))  # Best case T(N) = O(N) + 2(N/2) -> T(N) = O(NlogN)
