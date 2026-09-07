#First way: Withot function 

num=12
square=num*num

print(square)

print("-----------")
 
#Second Way : Using function
def square(num):  #parameter--> defining in function
    return num*num
 
result=square(12)  #12 is argument
#Calling a function / using a function / involking
print(result)



"""
def → tells Python we're defining a function
square → function name
number → parameter
return → sends result back
"""