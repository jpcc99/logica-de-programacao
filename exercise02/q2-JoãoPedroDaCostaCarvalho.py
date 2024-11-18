factory_costs = float(input("Digite o custo de fábrica: "))
while factory_costs < 0.0:
    print("Números negativos não são permitidos!")
    factory_costs = float(input("Digite novamente: "))

taxes_percentage = 0.0
distributor_percentage = 0.0

if factory_costs < 35000.00:
    distributor_percentage = factory_costs * 0.05
    taxes_percentage = 0.0
elif factory_costs >= 35000.00 and factory_costs < 70000.00:
    distributor_percentage = factory_costs * 0.10
    taxes_percentage = factory_costs * 0.15
else:
    distributor_percentage = factory_costs * 0.15
    taxes_percentage = factory_costs * 0.20

new_car_price = factory_costs + distributor_percentage + taxes_percentage

print(f"R$ {new_car_price:.2f}")