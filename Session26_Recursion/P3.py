for i in range(1,11):
    print(i)
    
print("-------------")


def print_numbers(num):
    # 1. Base Case 
    if num==11:
        return 
    
    # 2. Work 
    print(num)
    
    # 3. Recursive call
    print_numbers(num+1)


print_numbers(1)


