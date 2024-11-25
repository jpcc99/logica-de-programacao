num = -1
is_prime = False

while num < 0:
    num = int(input("Digite um número inteiro maior que zero: "))

match num:
    case 1: 
        is_prime = True
    case 2:
        is_prime = True
    case _:
        if num % 2 != 0:
            for i in range(3, num):
                if num % i == 0:
                    is_prime = False
                    break
                is_prime = True
        else:
            is_prime = False

if is_prime:
    print("Sim")
else:
    print("Não")
