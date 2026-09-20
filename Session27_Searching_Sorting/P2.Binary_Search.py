def Binary_Search(arr, target):
    # Prerequisite
    arr.sort()
    n = len(arr)

    low = 0
    high = n - 1

    while low <= high:
        # Step1 : finding mid
        mid = (low + high) // 2

        # Case 1:
        if arr[mid] == target:
            return True

        # Case 2:
        elif arr[mid] < target:
            low = mid + 1

        # Case 3:
        else:
            high = mid - 1


    return False


arr = [12, 8, -2, 0, 1, 99, 11, 3, 4]
target = 100

ans = Binary_Search(arr, target)
print("Output :", ans)
