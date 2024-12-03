num = 1 
sum = 0

while num > 0:
    num = int(input("Digite um inteiro: "))
    if num == 0: 
        break
    elif num < 0:
        print("O número deve ser positivo!") 
        continue

    if num <= 3:
        sum += num
        continue
    elif num % 2 == 0:
        continue

    is_prime = True
    for i in range(num - 1, 2, -1):
        if num % i == 0:
            is_prime = False

    if is_prime:
        sum += num

print(sum)
