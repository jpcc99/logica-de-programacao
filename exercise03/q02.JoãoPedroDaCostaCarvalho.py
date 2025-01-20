def get_int_list_input_for(a_list):
    items = str(input()).split(" ")
    for item in items:
        a_list.append(int(item))

list_a = []
list_b = []
list_c = []

get_int_list_input_for(list_a)
get_int_list_input_for(list_b)

for i in list_a:
    if i not in list_c:
        list_c.append(i)

for i in list_b:
    if i not in list_c:
        list_c.append(i)

print(list_c)
    