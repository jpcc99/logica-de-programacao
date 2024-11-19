entry = float(input("Digite a entrada: "))
installments_code = int(input("Digite o código da forma de pagamento: "))

descounted_price = 0.0

match installments_code:
    case 1:
        descounted_price = entry - entry * 0.30
        print(f"1x de (à vista) R$ {descounted_price:.2f}")
    case 2:
        installments_price = entry / 2
        descounted_price = installments_price - installments_price * 0.20
        print(f"2x de R$ {descounted_price:.2f}")

    case 3:
        installments_price = entry / 3
        descounted_price = installments_price - installments_price * 0.10
        print(f"3x de R$ {descounted_price:.2f}")

    case 4:
        descounted_price = entry / 4
        print(f"4x de R$ {descounted_price:.2f}")

    case _:
        print("ERRO")