#calcula a média de notas usando os conceitos M1 e M2 da UMC

materia = int(input("Escolha a matéria: \n Software Básico = 1 \n Redes e Seguranca = 2 \n"))


if materia == 1:
    print("Você selecionou Software Básico. \n")
elif materia == 2:
    print("Você selecionou Redes e Segurança. \n")
else:
    print("Matéria inválida. \n")

m1 = int(input("Digite sua M1: "))
m2 = int(input("Digite sua M2: "))


mfinal = m1 + (m2 * 2) / 3
print(f"Sua média final é {mfinal}")