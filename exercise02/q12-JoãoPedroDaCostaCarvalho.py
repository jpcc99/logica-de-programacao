base = int(input("Digite a base da potência: "))
exponent = int(input("Digite o expoente: "))
power = int(1)
for i in range(exponent):
    power *= base

print(power)

