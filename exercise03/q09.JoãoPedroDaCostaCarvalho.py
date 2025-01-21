temperatures = [int(i) for i in input("").split(" ")]


def find_max_in(temperatures):
    max_i = 0
    max_temp = temperatures[0]
    for i in range(1, len(temperatures)):
        if temperatures[i] > max_temp:
            max_temp = temperatures[i]
            max_i = i
    return [max_i, max_temp]


def find_min_in(temperatures):
    min_i = 0
    min_temp = temperatures[0]
    for i in range(1, len(temperatures)):
        if temperatures[i] < min_temp:
            min_temp = temperatures[i]
            min_i = i
    return [min_i, min_temp]


def get_month_by(index):
    match index:
        case 0:
            return "JANEIRO"
        case 1:
            return "FEVEREIRO"
        case 2:
            return "MARÇO"
        case 3:
            return "ABRIL"
        case 4:
            return "MAIO"
        case 5:
            return "JUNHO"
        case 6:
            return "JULHO"
        case 7:
            return "AGOSTO"
        case 8:
            return "SETEMBRO"
        case 9:
            return "OUTUBRO"
        case 10:
            return "NOVEMBRO"
        case 11:
            return "DEZEMBRO"


max_month_and_temp = find_max_in(temperatures)
max_month = get_month_by(max_month_and_temp[0])
min_month_and_temp = find_min_in(temperatures)
min_month = get_month_by(min_month_and_temp[0])
print(f"MAIOR: {max_month_and_temp[1]}ºC em {max_month}")
print(f"MENOR: {min_month_and_temp[1]}ºC em {min_month}")
