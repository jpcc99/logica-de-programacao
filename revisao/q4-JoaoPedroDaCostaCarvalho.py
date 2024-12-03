num = int(input("Digite um número: "))
qtd = 0

for i in range(1, num + 1):
    if num % i == 0:
        qtd += 1

print(qtd)
