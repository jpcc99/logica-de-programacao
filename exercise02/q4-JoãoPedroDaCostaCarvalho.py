fst_angle = int(input("Digite o 1º ângulo: "))
snd_angle = int(input("Digite o 2º ângulo: "))
trd_angle = int(input("Digite o 3º ângulo: "))


if (fst_angle + snd_angle + trd_angle) > 180:
    print("Triângulo inválido")

if fst_angle < 90 and snd_angle < 90 and trd_angle < 90:
    print("Acutângulo")
elif fst_angle == 90 or snd_angle == 90 or trd_angle == 90:
    print("Retângulo")
else:
    print("Obtusângulo")
