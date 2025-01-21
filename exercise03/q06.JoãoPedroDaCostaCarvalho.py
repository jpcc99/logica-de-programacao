def is_positive(num):
    if num >= 0:
        return "POSITIVO"
    else:
        return "NEGATIVO"


input = int(input(""))
print(is_positive(input))
