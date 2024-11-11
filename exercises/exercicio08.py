n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

avg = (n1 + n2) / 2

if avg < 3.0:
    print(f"{avg:.1f}-Reprovado")
elif 3.0 <= avg < 7:
    print(f"{avg:.1f}-Exame")
else:
    print(f"{avg:.1f}-Aprovado")