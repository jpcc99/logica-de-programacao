avg = 0.0
num_of_grades = 0
sum_of_grades = 0.0

print("Digite notas do estudante e para parar digite um número negatio")
while True:
    grade = float(input("Nota: "))

    if grade < 0.0:
        if sum_of_grades != 0.0:
            avg = sum_of_grades / num_of_grades
            print(f"{avg:.1f}")
        break

    num_of_grades += 1
    sum_of_grades += grade


