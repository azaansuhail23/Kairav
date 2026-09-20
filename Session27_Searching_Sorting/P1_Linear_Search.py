def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return False

arr = [12, 8, -2, 0, 1, 99, 11, 3, 4]
target = 7

ans=Linear_Search(arr,target)
print("Output :", ans)