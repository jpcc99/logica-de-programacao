n = int(input())


def do_sum_between(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print(do_sum_between(n))
