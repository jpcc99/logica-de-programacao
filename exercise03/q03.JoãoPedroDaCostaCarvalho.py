numbers = [int(i) for i in input("").split(" ")]

step = 6
for i in range(0, len(numbers), step):
    for j in range(i, step + i):
        print(numbers[j], end=" ")
    print()
