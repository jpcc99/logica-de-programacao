MINIMUM_WAGE = 1212.00
salary = float(input("Digite o salário do colaborador: "))

new_salary = None
if salary <= MINIMUM_WAGE:
    new_salary = salary * 1.20
else:
    new_salary = salary * 1.15

print(f"R$ {new_salary:.2f}")