# 8) Elaborar um programa que o usuário deva preencher uma lista com 20 números
# inteiros. Após preencher a lista o programa deve verificar para cada número, se
# ele é primo ou não. O programa deve armazenar apenas os números primos em uma
# nova lista. Exiba a lista de primos e a quantidade encontrada.

lista = []
primosl = []

for i in range(20):
    num = int(input(f"Digite o {i + 1}º número: "))
    lista.append(num)

for num in lista:
    primo = True

    if num <= 1:
        primo = False
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                primo = False
                break

    if primo == True:
        primosl.append(num)

print(f"numeros primos: {primosl}, {len(primosl)}x")