product_code = int(input("Digite o código da fruta: "))
weight = float(input("Digite o peso da fruta em kg: "))
product_name = ""
price = 0.0

match product_code:
    case 1:
        product_name = "Maçã"
        if weight <= 5:
            price = 7.00 * weight
        else:
            price = 5.80 * weight
    case 2:
        product_name = "Pêra"
        if weight <= 5:
            price = 11.80 * weight
        else:
            price = 8.50 * weight
    case 3:
        product_name = "Laranja"
        if weight <= 5:
            price = 2.25 * weight
        else:
            price = 1.70 * weight
    case 4:
        product_name = "Banana"
        if weight <= 5:
            price = 5.50 * weight
        else:
            price = 4.00 * weight
    case 5:
        product_name = "Tomate"
        if weight <= 5:
            price = 6.90 * weight
        else:
            price = 5.50 * weight
    case 6:
        product_name = "Cebola"
        if weight <= 5:
            price = 4.50 * weight
        else:
            price = 2.40 * weight
    case _ :
        print("Código inválido!")

print(f"R$ {price:.2f}")