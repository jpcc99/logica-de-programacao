list_a = [int(i) for i in input("").split(" ")]
list_b = [int(i) for i in input("").split(" ")]
list_c = []

def extend_if_not_in(list_a, list_b):
    for i in list_a:
        if i not in list_b:
            list_b.append(i)


extend_if_not_in(list_a, list_c)
extend_if_not_in(list_b, list_c)

print(list_c)
