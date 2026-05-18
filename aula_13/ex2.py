# 2) Elaborar um programa em que o usuário deva preencher uma lista com 30 números.
# Após o preenchimento o programa deve calcular a média dos números inseridos. Logo
# em seguida, o programa deve salvar em outra lista somente os números que são
# maiores que a média. Exibir no final a lista dos números maiores que a média.

lista = []

divisor = 0
for i in range(30):
    num = int(input(f"aloque uma posição ao índice {i}: "))
    lista.append(num)

    dividendo = sum(lista)
    divisor += 1

media = dividendo / divisor


lista2 = lista[:]
for numero in lista:
    if numero < media:
       lista2.remove(numero)

print(f"soma de todos os indices:", dividendo)
print(f"quantidade de números a ser dividido: ", divisor)
print(f"resultado da media: ", media)


print(f"valores a cima de {int(media)} arrendondo = {media:.0f}: ", lista2)