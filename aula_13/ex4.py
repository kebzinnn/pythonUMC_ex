# 4) Elaborar um programa para uma loja que possui uma lista contendo a quantidade
# de itens em estoque para diversos produtos. Crie um programa que o usuário deva
# preencher o nome dos produtos e quantidade deste produto (uma lista para o nome
# e uma lista para quantidade). Classifique cada item como: "Estoque crítico"
# (quantidade menor que 5) ou "Estoque baixo" (entre 5 e 10) ou "Estoque normal"
# (acima de 10). Gere uma nova lista contendo apenas os produtos com estoque
# crítico. Exiba essa lista ao final.

nomel = []
qtdl = []
critico = []
baixo = []
normal = []
for i in range(3):
    nome = str(input(f"Digite o nome para o {i + 1}º produto: "))
    nomel.append(nome)
    qtd = int(input(f"Digite a quantidade para o {nome}: "))
    qtdl.append(qtd)

#for i in range(len(qtdl)):
    #qtd = qtdl[i]
    #nome = nomel[i]
produtos_ordenados = sorted(zip(qtdl, nomel)) #sorted deixa em ordem crescente e zip agrupa as duas listas

for qtd, nome in produtos_ordenados:
    formatacao = f"{nome} ({qtd})"

    if qtd < 5:
        critico.append(formatacao)
    elif qtd <= 10:
        baixo.append(formatacao)
    else:
        normal.append(formatacao)

print("critico: ", critico)
print("baixo: ", baixo)
print("normal:", normal)