#calcula a média de notas usando M1 e M2 da UMC com conceitos básicos

materia = int(input("Escolha a matéria: \n Software Básico = 1 \n Redes e Seguranca = 2 \n"))


if materia == 1:
    print("Você selecionou Software Básico. \n")
elif materia == 2:
    print("Você selecionou Redes e Segurança. \n")
else:
    print("Matéria inválida. \n")

m1 = -1
m2 = -1

while m1 < 0 or m1 > 10:
    m1 = float(input("Digite sua M1: "))
    
    if m1 < 0:
        print("Nota inválida (Valor mínimo = 1)")
    elif m1 > 10:
        print("Nota inválida (Valor máximo = 10)")

while m2 < 0 or m2 > 10:
    m2 = float(input("Digite sua M2: "))

    if m2 < 0:
        print("Nota inválida (Valor mínimo = 1)")
    if m2 > 10:
        print("Nota inválida. (Valor máximo = 10)")

mfinal = (m1 + (m2 * 2)) / 3
print(f"Sua média final é {mfinal}")