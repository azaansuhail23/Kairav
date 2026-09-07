def local_scope():
    x=10
    print(x)

local_scope()
# print(x)   #!It will throw error if you accessed local variable outside the function scope.

print("----------")

y=12
def global_scope():
    print("Inside the global scope function : ",y)


global_scope()
print("Outside the global scope function : ",y)