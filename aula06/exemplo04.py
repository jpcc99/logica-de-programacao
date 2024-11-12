i = int(input("Digite um número: "))
while i >= 0:
    if i % 2 == 0:
        print("É par")
    else: 
        print("É ímpar")
    i = int(input("Digite um número: "))
else:
    print(f"{i} é negativo.")