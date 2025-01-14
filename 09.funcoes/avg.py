def do_sum(a_list):
    total = 0
    for i in a_list:
        total += i
    return total

def avg(a_list):
    avg = do_sum(a_list) / len(a_list)
    return avg

print(avg([3, 2, 6, 7, 10]))