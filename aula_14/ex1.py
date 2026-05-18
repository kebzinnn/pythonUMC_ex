matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um valor: ")))
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        print(matriz[i][j])