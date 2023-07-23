def maxSubArr(arr):
    maxSub = arr[0]
    curMax = 0
    for n in arr:
        if curMax < 0:
            curMax = 0
        curMax += n
        maxSub = max(curMax, maxSub)
    return maxSub


arr = [10, 2, -3, -1]
ans = maxSubArr(arr)  # O(n)
print(ans)


def bin(arr, i, j, x):
    if i > j:
        return -1
    mid = (i+j) // 2
    if x == arr[mid]:
        return mid
    if x < arr[mid]:
        return bin(arr, i, mid-1, x)
    if x > arr[mid]:
        return bin(arr, mid+1, j, x)


arr = [10, 45, 67, 89, 101, 221]
ans = bin(arr, 0,  len(arr)-1, 101)
print(ans)


def ternary(arr, l, h, x):
    while l <= h:
        mid1 = l + (h - l) // 3
        mid2 = h - (h - l) // 3

        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2

        else:
            if x < arr[mid1]:
                h = mid1 - 1
            elif x > arr[mid2]:
                l = mid2 + 1
            else:
                h = mid1 + 1
                l = mid2 - 1

    return -1


arr = [10, 45, 67, 89, 101, 221]
ans = ternary(arr, 0,  len(arr)-1, 101)
print(ans)
