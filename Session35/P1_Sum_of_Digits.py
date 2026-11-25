def Sum_Digits(num):
    sum = 0

    while num > 0:
        # finding last digit of a num
        last_digit = num % 10

        sum += last_digit

        # divide the no.
        num = num // 10
    
    print(sum)
    
Sum_Digits(41253)