a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

bigger_ab = None
bigest = None

if a > b: 
    bigger_ab = a
else:
    bigger_ab = b

if bigger_ab > c:
    bigest = bigger_ab
else:
    bigest = c

print(f"{bigest:.0f}")