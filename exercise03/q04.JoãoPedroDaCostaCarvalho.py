def str_validation(string, min_num, max_num):
    return min_num < len(string) < max_num


input = str(input()).split(",")
s = input[0]
min = int(input[1])
max = int(input[2])


print(str_validation(s, min, max))
