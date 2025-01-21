list_a = [int(i) for i in input("").split(" ")]
list_b = [int(i) for i in input("").split(" ")]
list_c = []

for i in list_a:
    if i not in list_c:
        list_c.append(i)

for i in list_b:
    if i not in list_c:
        list_c.append(i)

print(list_c)
