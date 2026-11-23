def merge_arrays(arr, si, mid, ei):
    temp = []

    i = si  # for--> left part
    j = mid + 1  # for --> Right part

    # comparing both halves
    while i <= mid and j <= ei:
        if arr[i] < arr[j]:
            temp.append(arr[i])

            i += 1
        else:
            temp.append(arr[j])

            j += 1

    # Remaining in the left portion
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Remain in the right portion
    while j <= ei:
        temp.append(arr[j])
        j += 1

    # copying back to original
    for p in range(len(temp)):
        arr[si + p] = temp[p]


def Merge_Sort(arr, si, ei):
    # Base : Single element is always sorted
    if si == ei:
        return

    mid = (si + ei) // 2

    # left recursion call
    Merge_Sort(arr, si, mid)
    # right recursion call
    Merge_Sort(arr, mid + 1, ei)

    # Conquer/Join function
    merge_arrays(arr, si, mid, ei)

arr=[17,1,8,9,3,19,75,5]

print("Before Sorting:",arr)
Merge_Sort(arr,0,len(arr)-1)
print("After Sorting:",arr)