a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

bigger_ab = (a + b + abs(a - b)) / 2
bigger = (bigger_ab + c + abs(bigger_ab - c)) / 2

print(f"{bigger:.0f} é o maior")