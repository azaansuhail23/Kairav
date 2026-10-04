def Selection_Sort(list):
    n=len(list)
    i = 0  # Swapping pointer

    while i < n - 1:
        min_element = min(list[i:])
        idx = list.index(min_element, i)

        list[i], list[idx] = list[idx], list[i]

        i = i + 1


list = [12, 25, 64, 11, 22]

# Calling this function
print("Before: ", list)

Selection_Sort(list)

print("After: ", list)
