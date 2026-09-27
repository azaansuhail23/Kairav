def Swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]


def Bubble_Sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                Swap(arr, j, j + 1)


arr = [2, 10, 8, 7]
print("Before: ",arr)

Bubble_Sort(arr)

print("After: ",arr)


# Visualization : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/
