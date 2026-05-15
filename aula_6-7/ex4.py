# Elabore um algoritmo que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. 
# Caso o usuário digite um número fora desse intervalo, o algoritmo mostra uma mensagem informando “Número inválido”.

numero = int(input("Digite um número para saber qual o dia da semana (1): "))

if numero > 7 or numero < 1:
    print("Número invalido")
else:
    if numero == 1:
        print("Domingo")
    elif numero == 2:
        print("Segunda")
    elif numero == 3:
        print("Terça")
    elif numero == 4:
        print("Quarta")
    elif numero == 5:
        print("Quinta")
    elif numero == 6: 
        print("Sexta")
    elif numero == 7:
        print("Sábado")