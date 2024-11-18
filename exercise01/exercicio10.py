a = int(input("a: "))
b = int(input("b: "))
op = int(input("op: "))

match op:
    case 1:
        pow_ab = a ** b
        print(f"{pow_ab:.1f}")
    case 2:
        sum_of_squares = a ** 2 + b ** 2
        print(f"{sum_of_squares:.1f}")
    case 3:
        sum_of_sqrts = (a ** (1 / 2)) + (b ** (1 / 2))
        print(f"{sum_of_sqrts:.1f}")
    case _:
        print("ERRO")