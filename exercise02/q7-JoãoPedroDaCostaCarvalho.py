fact = int(input("Digite o num para saber o fatorial: "))
i = fact - 1

if fact == 0:
    print(1)
else:
    while i >= 1:
        fact *= i
        i -= 1

print(fact)