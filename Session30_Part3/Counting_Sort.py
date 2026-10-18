def Counting_Sort(list):
    # Step1 : Finding the maximum element from the list
    max_element = max(list)

    # Step2 : Initialize a frequency list of size max+1
    freq = [0] * (max_element + 1)

    # Step3 : Storing the freqency of every element in the frequency list
    for i in range(len(list)):
        freq[list[i]] += 1

    # Step 4: Final sorting
    j = 0
    for i in range(len(freq)):
        while freq[i] > 0:
            list[j] = i
            j += 1

            freq[i] -= 1


arr=[5,4,4,3,1,7,7,2,5,8,7,6,5,3,2,2]

print("Before Sorting : ",arr)

Counting_Sort(arr)

print("After Sorting : ", arr)