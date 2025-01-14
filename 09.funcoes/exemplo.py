def is_even(x):
    return x % 2 == 0

print(is_even(2))
print(is_even(3))
print(is_even(10))

def is_even_or_odd(x):
    if is_even(x):
        return "Even"
    else:
        return "Odd"
    
print(is_even_or_odd(2))
print(is_even_or_odd(3))