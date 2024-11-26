n = 0
m = 1
buf = ""

while True:
    n = int(input("n: "))
    m = int(input("m: "))
    
    if n > m: 
        break

    sum_between_pairs = 0
    for i in range(n, m + 1):
        sum_between_pairs += i
    
    buf += str(sum_between_pairs) + " "
    

print(buf)
