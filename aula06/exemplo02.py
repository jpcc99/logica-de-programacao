num = int(input())

i = 1
while i <= num and num <=0:
    if i % 2 == 0:
        print(i)
        i += 1
else:
    print("Número negativo")