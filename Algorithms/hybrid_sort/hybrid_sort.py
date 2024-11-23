# Modify the code so that any subarray with 10 or fewer elements will be sorted using insertion sort rather than a recursive mergesort.
#
# (This is actually an optimization; for arrays that are this small, insertion sort will generally be faster than mergesort.)
#
# Implement a further optimization: if merge() needs to merge two adjacent subarrays and sees that the last element of the first subarray and the first element of the second subarray are in order, then it can return immediately since there is nothing to do.
#
# (This can greatly improve mergesort's performance in situations where the input array is already sorted or is nearly sorted).
#
# Modify the code to explain what it is doing as it runs:
#
# When the code begins sorting any subarray, print 'sorting' followed by a description of the subarray.
#
# After the subarray sort is complete, print 'sorted' followed by a description of the sorted subarray.
#
# The subarray descriptions should match the sample output below. If a subarray has 10 or fewer elements, list all its elements.
#
# Otherwise, print only the first five, followed an ellipsis ("...") and then the last five.
#
# If a subarray is sorted using insertion sort, print 'insertion sort' followed by the number of comparisons that the insertion sort performed.
#
# When two subarrays are merged, describe the merge as in the sample output below. If the merge is skipped, print 'skipped merge!'
#
# Indent the output by four spaces for each level of recursion.
#
# Finally, add top-level code that reads a single line of standard input containing integers to be sorted, separated by spaces. The code should sort the integers using your sorting implementation. You don't need to print out the sorted sequence at the end; the output from step 4 above is enough.

def insertion_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        t = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > t:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = t


    print(f"{count}*      +" "insertion sort ({count} compares")

def merge(arr, d, e, f):
    print(f"sorting a[]")
    a = arr[d:e]  # copy of left half
    b = arr[e:f]  # copy of right half

    i = 0  # index into a
    j = 0  # index into b

    for k in range(d, f):
        if i == len(a):  # a has no more elements
            arr[k] = b[j]
            j += 1
        elif j == len(b):  # b has no more elements
            arr[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1


# sort only elements a[i:j], i.e. a[i .. (j - 1)]
def merge_sort_range(a, i, j, count = 0):
    if j - i < 2:
        return
    print(count)
    print(f"sorting a[{i}:{j}] = {a}")
    mid = (i + j) // 2
    if len(a) <= 10:
        insertion_sort(a)
    else:
        count += 1
        merge_sort_range(a, i, mid, count)  # recursively sort left half
        merge_sort_range(a, mid, j, count)  # recursively sort right half

    merge(a, i, mid, j)  # merge left and right halves together


# merge sort an entire array
def merge_sort(a):
    merge_sort_range(a, 0, len(a))
    print(f"sorted a = {a}")



arr = [4, 2, 6, 8, 10, 1, 17, 3, 5, 18, 9, 1, 5, 20, 0, 100]


merge_sort(arr)
print(arr)