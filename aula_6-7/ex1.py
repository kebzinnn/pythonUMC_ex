# Elabore um algoritmo que leia dois números e apresente-os em ordem crescente.

# usando lógica de programação

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if num1 <= num2:
    print(f"Ordem crescente: {num1}, {num2}")
elif num1 >= num2:
    print(f"Ordem crescente: {num2}, {num1}")

# usando lista ".sort()"

n1 = float(input("Numero 1: "))
n2 = float(input("Número 2: "))

lista = [n1, n2]

lista.sort()

print(f"Ordem crescente: {lista[0]:g}, {lista[1]}") # ":g" ex: se o valor fosse 2.5 imprimiria 2.5, já se fosse 1, em vez de ficar 1.0 ele tira o valor 0 (inutil)