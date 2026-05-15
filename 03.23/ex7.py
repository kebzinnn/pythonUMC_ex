# Um determinado clube de futebol pretende classificar seus atletas em categorias e, para isso,
# contratou um programador para criar um programa que executasse essa tarefa.

# Para isso, o clube criou uma tabela que contém a faixa etária do atleta e sua categoria.

# Como ficaria esse programa?

# Tabela:

# De 05 a 10 anos → Infantil
# De 11 a 15 anos → Juvenil
# De 16 a 20 anos → Júnior
# De 21 a 25 anos → Profissional

print("De 05 a 10 anos → Infantil \nDe 11 a 15 anos → Juvenil\nDe 16 a 20 anos → Júnior\nDe 21 a 25 anos → Profissional\n")

idade = int(input("Digite a idade do atleta: "))

if idade < 5 or idade > 25:
    print("Idades disponiveis: (5 a 25 anos)")
elif idade <= 10:
    print("Categoria infantil")
elif idade <= 15:
    print("Categoria Juvenil")
elif idade <= 20:
    print("Categoria Júnior")
elif idade <= 25:
    print("Categoria Profissional")