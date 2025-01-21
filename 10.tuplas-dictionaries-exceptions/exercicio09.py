try:
    value = int(input("Entre um valor: "))
    print(value / value)

except: ValueError:
    print("Entrada incorreta")
except ZeroDivisionError:
    print("Entrada muito ruim")
except:
    print("Boo!")