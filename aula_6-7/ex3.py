# Elaborar um algoritmo que deve receber um número qualquer e exibir se ele é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("o número é par, pois o resto da sua div por 2 (mod2) é igual a 0.")
else:
    print("o número é impar, pois o resto da sua div por 2 (mod2) é maior que 0.")