stack=[]

#Operation 1 : Push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

#Operation 2 : Pop
removed=stack.pop()
print("Removed Element:",removed)
print(stack)


#Operation 3 : Peek
print("Peek Element:",stack[-1])


#Operation 4 : isEmpty 
stack2=[]

if len(stack2)==0:
    print("Stack is empty")
else:
    print("Stack is not empty")
    
#Operation 5 : Size of Stack
print(len(stack))