# 3) Elaborar um programa que dada uma lista com 15 números inteiros (inseridos
# pelo usuário), o programa deve a partir desta lista criar uma nova lista seguindo
# as seguintes regras: para números pares deve armazene o seu quadrado; se forem
# ímpares, armazene o seu cubo. Ao final, exiba a nova lista ordenada em ordem
# crescente.

lista = []

for i in range(15):
    num = int(input(f"Digite o indice {i}: "))
    lista.append(num)

lista2 = []

for i in lista:
    if (i % 2) == 0:
        lista2.append(i ** 2)
    else:
        lista2.append(i ** 3)

pares = []
impares = []

for i in lista:
    if (i % 2) == 0:
        pares.append(i ** 2)
    else:
        impares.append(i ** 3)

lista2.sort()   
print(lista2)
print(f"números pares: {pares}")
print(f"números impares: {impares}")