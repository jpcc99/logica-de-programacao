avg_salary = float(input("Digite seu salário médio: "))
while avg_salary < 0.0:
    print("Seu salário médio não pode ser negativo.")
    avg_salary = float(input("Digite novamente:")) 
    
special_credit = None

if avg_salary <= 200.00:
    special_credit = avg_salary * 0.10
elif avg_salary > 200.00 and avg_salary <= 300.00:
    special_credit = avg_salary * 0.20
elif avg_salary > 300.00 and avg_salary <= 400.00:
    special_credit = avg_salary * 0.25
else:
    special_credit = avg_salary * 0.30

print(f"R$ {special_credit:.2f}")