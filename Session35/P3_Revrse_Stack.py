#Approach 1 : Inbuilt Class
stack1 = [10, 20, 30, 40]

stack1.reverse()

print(stack1)

#Approach 2 : External Stack

stack=[10,20,30,40]
temp=[]

while len(stack)>0:
    element=stack.pop()
    temp.append(element)

stack=temp
print(temp)
