def binary_search(a, n, searchValue):
    first = 0
    last = n-1
    while first <=last:
        mid = (first + last) // 2
        if searchValue < a[mid]:
            last = mid - 1
        elif searchValue > a[mid]:
            first = mid + 1
        else:
            return mid
    return -1
