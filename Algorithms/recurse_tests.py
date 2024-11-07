# return the sum of 1+2+....+n        T(N) = O(1) + T(N-1) -> O(N)


def sum(n):
    if n == 0:
        return 0

    return n + sum(n - 1)


# return the sum of all elements in a.     T(N) = O(N) + T(N-1) -> O(N^2)


def sum_array(a):
    if a == []:
        return 0

    return a[0] + sum_array(a[1:])


def foo(n):  # ->foo(N) almost = log(base 2) N       T(N) = O(1) + T(N/2) -> O(logN)
    if n == 0:
        return 0

    return 1 + foo(n // 2)
