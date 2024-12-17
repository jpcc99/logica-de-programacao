numbers = []

for i in range(5):
    x = int(input("Digite o número: "))
    numbers.append(x)


sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

avg = sum / len(numbers)

print("Numbers: ", numbers)
print("Sum: ", sum)
print(f"Average: {avg:.2f}")
