x = int(input("Distância total percorrida (em km): "))
y = float(input("Total de combustível gasto (em litros): ")) # 1 casa decimal

km_per_l = float(x) / y

print(f"{km_per_l:.3f} km/l")