count_victories = 0
result = ""
count = 0

while result != -1 and count <= 5:
    result = str(input("Digite o resultado da partida: "))
    if result == "-1":
        break
    match result.upper():
        case "V":
            count_victories += 1
            count += 1
        case "P":
            count += 1
            continue
        case _: 
            print("Digite apenas V ou P")
            continue
    
if count_victories == 0:
    print("-1")
elif count_victories <= 2:
    print("3")
elif count_victories <= 4:
    print("2")
elif count_victories <= 6:
    print("1")

