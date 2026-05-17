# calcula a média de notas usando M1 e M2 da UMC usando o conceito de dicionario para definir qual materia foi escolhida
# dicionario = {
#     1: "x",
#     2: "y"
# }

materias_disp = {
    1: "Software Básico",
    2: "Redes e Segurança"
}

materia = int(input("\n Software Básico = 1 \n Redes e Seguranca = 2 \n Digite sua matéria: "))

materia_nome = materias_disp.get(materia, "erro")

if materia_nome == "erro":
    print("Máteria inexistente")
else:
    print(f"Você escolheu {materia_nome}")

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

#utiliza .2f para definir a qtd de casas decimais após o ponto em duas e puxa {materia_nome} para dizer qual foi a materia escolhida lá no começo
print(f"Sua média final em {materia_nome} é {mfinal:.2f}") 