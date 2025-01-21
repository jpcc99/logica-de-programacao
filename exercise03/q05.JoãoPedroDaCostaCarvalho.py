def calc_pow(x, z):
    prod = x
    for _ in range(1, z):
        prod *= x
    return prod


input = str(input("")).split(" ")
x = int(input[0])
z = int(input[1])

print(calc_pow(x, z))
