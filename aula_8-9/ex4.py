# Elaborar um algoritmo que lê um número N inteiro maior que 2. 
# Logo após o programa deve exibir o quadrado e o cubo de 2 até N.

while True:
    n = int(input("Digite um numero: "))

    if n > 2:
        for i in range(2, n + 1):
            quadrado = i ** 2
            cubo = i ** 3
            print(f"Quadrado de {i}: {quadrado}, cubo: {cubo}")
    else:
        print("Número deve ser maior que 2")