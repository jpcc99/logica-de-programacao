dog_year = -1
while dog_year < 0:
    dog_year = int(input("Digite a idade do cão: "))

human_years = 0
for i in range(1, dog_year + 1):
    if i <= 2:
        human_years += 21
    elif i <= 4:
        human_years += 5
    elif i <= 7:
        human_years += 3
    else:
        human_years += 2

print(human_years)
