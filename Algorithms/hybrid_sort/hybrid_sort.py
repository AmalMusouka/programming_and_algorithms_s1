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

# insertion sort for an array a
def insertion_sort(a, i, j, count):
    compare = 0
    s = '    '
    for index in range(i,j):
        t = a[index]
        prev = index - 1

        while prev >= i and a[prev] > t:
            compare += 1
            a[prev + 1] = a[prev]
            prev -= 1
        if (prev >=i) and not (a[prev] > t):
            compare += 1
        a[prev + 1] = t
    count += 1
    print(f"{count * s}insertion sort ({compare} compares)")


# merge sorted subarrays arr[d:e] and arr[e:f] into the subarray arr[d:f]
def merge(arr, d, e, f):
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

def is_sorted(a, i, j):
    for index in range(i, j - 1):
        if a[index] > a[index + 1]:
            return False

    return True


# sort only elements a[i:j], i.e. a[i .. (j - 1)]
def merge_sort_range(a, i, j, count):
    if j - i < 2 and not (len(a) <= 1):
        return
    count+= 1
    mid = (i + j) // 2
    s = '    '

    if len(a[i:j]) <= 10 or len(a) <= 1:
        string = ' '.join(str(value) for value in a[i:j])
        print(f"{count * s}sorting a[{i}:{j}] = [{string}]")
        if len(a) > 1:
            insertion_sort(a, i, j, count)

        new_string = ' '.join(str(value) for value in a[i:j])
        print(f"{count * s}sorted a[{i}:{j}] = [{new_string}]")
    else:
        left = ' '.join(str(value) for value in a[i:i+5])
        right = ' '.join(str(value) for value in a[j-5:j])
        print(f"{count * s}sorting a[{i}:{j}] = [{left} ... {right}]")

        merge_sort_range(a, i, mid, count)  # recursively sort left half
        merge_sort_range(a, mid, j, count) # recursively sort right half

        if not is_sorted(a, i, j) :
            merge(a, i, mid, j)# merge left and right halves together
            print(f"{(count+1) * s}merged a[{i}:{mid}] + a[{mid}:{j}] -> a[{i}:{j}]")
        else:
            print(f"{(count+1) * s}skipped merge!")

        new_left = ' '.join(str(value) for value in a[i:i+5])
        new_right = ' '.join(str(value) for value in a[j-5:j])
        print(f"{count * s}sorted a[{i}:{j}] = [{new_left} ... {new_right}]")



# merge sort an entire array
def merge_sort(a):
    count = -1
    merge_sort_range(a, 0, len(a), count)


string = str(input())
arr = [int(val) for val in string.split()]

merge_sort(arr)