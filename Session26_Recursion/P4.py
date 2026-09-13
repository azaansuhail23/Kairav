def decreasing(num):
    if num == 0:
        return

    print(num)

    decreasing(num - 1)


decreasing(10)
