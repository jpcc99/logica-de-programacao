numbers_input = str(input()).split(" ")
numbers = []
for number in numbers_input:
    numbers.append(int(number))

def is_prime(num):
    if num < 4:
        return True
    elif num >= 4 and num % 2 == 0:
        return False
    else:
        for i in range(4, num):
            if num % i == 0:
                return False
        return True
    
has_prime = False
for i in range(len(numbers)):
    num = numbers[i]
    if is_prime(num):
        has_prime = True
        print(f"{num} {i}")
if has_prime == False:
    print("-1-1")    
