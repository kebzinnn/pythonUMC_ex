# Elaborar um algoritmo que dados dois números fornecidos pelo usuário,
# faça uma calculadora para poder somá-los, subtraí-los, multiplicá-los e dividi-los, mostrando o resultado.

n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))

calc = str(input(f"Você escolheu {n1} e {n2}, qual operação gostaria de fazer? (+, -, *, /)"))

if calc == "+":
    print(n1 + n2)
elif calc == "-":
    print(n1 - n2)
elif calc == "*":
    print(n1 * n2)
elif calc == "/":
    if n2 == 0:
        print("Erro: divisão por 0.")
    else:
        print(n1 / n2)