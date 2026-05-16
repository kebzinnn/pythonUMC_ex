# Elaborar um algoritmo que recebe um número e só deve exibir o quadrado desse número se o número for positivo, 
# caso contrário o programa deve sempre solicitar um outro número até o usuário digitar um número positivo.

while True:
    num = float(input("Digite seu número inteiro: "))

    if num > 0:
        print(f"quadrado = {num**2}")
        break
