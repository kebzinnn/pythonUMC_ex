# Elaborar um programa que solicita um número de 10 a 15. Se o usuário digitar um número diferente, 
# o programa deve mostrar a mensagem "Entrada inválida" e solicitar um número novamente,
# se digitar correto o programa deve mostrar a raiz quadrada desse número e terminar.


while True:
    num = int(input("Digite um número de 10 a 15: "))

    if num in [10, 11, 12, 13, 14,15]:
        print(f"Raiz quadrada de {num} é igual a {num ** (1/2)}")
        break
    else:
        print("Número inválido, tente novamente!")

