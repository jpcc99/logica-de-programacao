a = int(input("Digite o 1º inteiro: "))
b = int(input("Digite o 2º inteiro: "))

if a > b:
    print("A não pode ser maior que B")

for a in range(a, b + 1):
    if a % 3 == 0:
        print(a, end=" ")
    a += 1