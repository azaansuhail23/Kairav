class Queue:
    def __init__ (self):
        self.stack1=[]
        self.stack2=[]

    # Insert element into queue
    def enqueue(self,element):
        self.stack1.append(element)

    # Remove element from queue
    def dequeue(self):
        # Transfer elements only when stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Queue is empty
        if not self.stack2:
            return -1

        return self.stack2.pop()

    # Get front element
    def front(self):
        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return -1;

        return self.stack2[-1]


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q.dequeue())  # 10
print(q.dequeue())  # 20

q.enqueue(50)

print(q.dequeue())  # 30
print(q.front())  # 40
print(q.dequeue())  # 40
print(q.dequeue())  # 50
print(q.dequeue())  # -1
