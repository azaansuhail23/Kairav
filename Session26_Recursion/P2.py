# Way1 : Loop
for i in range(5):
    print("Kairav")

print("----------")


def recursion_print(n):
    # Base Case :
    if n == 6:
        return

    print("Kairav")  # Work/task

    recursion_print(n + 1)  # Recusive call


recursion_print(1)
