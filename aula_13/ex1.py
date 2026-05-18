# 1) Elaborar um programa que contenha uma lista com 16 elementos em que o usuário
# deve preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário
# que digite dois números. Esses números devem corresponder a posições na lista
# (caso contrário solicite um novo valor). Após inserir os dois números o programa
# deve exibir a soma dos elementos das duas posições da lista.
lista = []

for i in range(16):
    a = float(input(f"Digite o {i + 1}º valor: "))
    lista.append(a)

    soma = 0

for i in range(2):
    b = int(input(f"Digite o {i + 1}º número (0 - {len(lista) - 1})"))

    if 0 <= b <= len(lista) - 1:
        soma += lista[b]
    else:
        print(f"Digite um número entre 0 a {len(lista) - 1}")

print(f"soma = {soma}")