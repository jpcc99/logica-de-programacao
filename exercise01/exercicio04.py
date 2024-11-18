x1 = float(input("Pont 1 x: "))
y1 = float(input("Pont 1 y: "))

x2 = float(input("Pont 2 x: "))
y2 = float(input("Pont 1 y: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

print(f"{distance:.4f}")