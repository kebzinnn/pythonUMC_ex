# Elaborar um algoritmo que solicite ao usuário vários valores inteiros. 
# Quando o usuário digitar 100 o programa deve terminar, 
# mostrando quantos valores foram acima de 80, 
# quantos foram abaixo de 10, 
# e mostrar a média de todos os valores digitados pelo usuário.

maior = 0
menor = 0
contador = 0
soma = 0

while True:
        num = int(input("Digite um valor inteiro: "))

        if num == 100:
            break

        if num > 80:
              maior += 1
        elif num < 10:
              menor += 1

        contador += 1
        soma += num

if contador > 0:
    media = soma / contador

    print(f"Quantos foram acima de 80: {maior}")
    print(f"Quantos foram abaixo de 10: {menor}")
    print(f"Soma = {soma}")
    print(f"Média = {media}")
