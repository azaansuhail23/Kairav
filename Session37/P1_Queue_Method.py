from collections import deque

q=deque()

#Enqueue Operation : 
q.append(10)
q.append(19)
q.append(88)
q.append(71)


#Note : You can add a element from the from as well
q.appendleft(11)
print(q)

#Deque Operation : 2 options available

#1.Removal from rear/back
print("Removal from back:",q.popleft())

#2.Removal from front(generally in all other programming languages)
print("Normal Removal(front):",q.pop())

#Front Opernation 
print("Front:",q[0])


#Rear Operation
print("Rear:",q[-1])

#Size / You can is Empty
if len(q)==0:
    print("IsEmpty")
else:
    print("Not Empty")
    

#Learn clear is a method to remove all the elements from the queue & making it empty
q.clear()
print(len(q)==0)