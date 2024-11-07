n = int(input())
ord_arr = [int(val) for val in input().split()]
seek_arr = [int(val) for val in input().split()]


def find_first(arr, target_num, size):
    low = 0
    high = size - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target_num:
            first = mid
            high = mid - 1

        elif arr[mid] > target_num:
            high = mid - 1
        else:
            low = mid + 1
    return first


def find_last(arr, target_num, size):
    low = 0
    high = size - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target_num:
            last = mid
            low = mid + 1

        elif arr[mid] > target_num:
            high = mid - 1
        else:
            low = mid + 1
    return last


for val in seek_arr:
    first_index = find_first(ord_arr, val, n)
    if first_index == -1:
        print(0)
    else:
        last_index = find_last(ord_arr, val, n)

        print(last_index - first_index + 1)
