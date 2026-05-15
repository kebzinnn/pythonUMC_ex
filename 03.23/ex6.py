# Uma empresa concederá um aumento de salário aos seus funcionários (variável de acordo com o cargo), conforme a tabela abaixo. 
# Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário.

# Se o cargo do funcionário não estiver na tabela, ele deverá receber 40% de aumento.

# Mostre o salário antigo, o novo salário e a diferença.

# Tabela de cargos e percentuais:

# 101 – Gerente – 10%
# 102 – Engenheiro – 20%
# 103 – Técnico – 30%

sal = int(input("Digite o salário: "))

print("Tabela de aumento: \n")
print("101 - Gerente: 10%")
print("102 - Engenheiro: 20%")
print("103 - Técnico: 30%")
print("Demais cargos: 40% \n")

cargo = str(input("Digite o cargo: \n")).lower()

print(f"\nSálario antigo: {sal}")

if cargo == "101" or cargo == "gerente":
    print("Sálario novo: ", sal * 1.10)
    print("Diferença: ", (sal * 1.10) - sal)
    print("Cargo escolhido: Gerente")
elif cargo == "102" or cargo == "engenheiro":
    print("Sálario novo: ", sal * 1.20)
    print("Diferença: ", (sal * 1.20) - sal)
    print("Cargo escolhido: Engenheiro")
elif cargo == "103" or cargo == "tecnico" or cargo == "técnico":
    print("Sálario novo: ", sal * 1.30)
    print("Diferença: ", (sal * 1.30) - sal)
    print("Cargo escolhido: Técnico")
else:
    print("Sálario novo: ", sal * 1.40)
    print("Diferença: ", (sal * 1.40) - sal)
    print(f"Cargo escolhido: {cargo}")