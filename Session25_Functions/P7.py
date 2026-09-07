# ? Parameters : You don't know how many parameters you are havin in your function.abs


def add(*num):  # ?args
    print(num)


add(10, 202, 303, 100, 45, -12)

print("------------")

def add_uncountable_paramenters(*nums):
    sum = 0

    for x in nums:
        sum += x

    return sum

res=add_uncountable_paramenters(10,20,30,40,12,99)
print(res)