limit = int(input("Digite o limite para impressão: "))
i = 1
while i <= limit:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1