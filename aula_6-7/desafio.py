import sys
# Faça um algoritmo, utilizando a estrutura escolha, para calcular a conta final de um hóspede de um hotel fictício, contendo:

# nome do hóspede;
# tipo do apartamento;
# número de diárias utilizadas;
# valor unitário da diária;
# valor total das diárias;
# valor do consumo interno;
# subtotal;
# valor da taxa de serviço;
# total geral;

# Considere que:
# Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias utilizadas pelo hóspede e o valor do consumo interno do hóspede

# o valor da diária é determinado pela seguinte tabela:

# Tipo de Apartamento Valor da diária (R$)
#       A                  150,00
#       B                  100,00
#       C                  75,00
#       D                  50,00

# o valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da diária;
# o subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
# o valor da taxa de serviço equivale a 10% do subtotal;
# a total geral resulta da soma do subtotal com a taxa de serviço

name = str(input("Qual o nome do hospede? "))
tipoapt = str(input("Escolha o tipo de apartamento (A, B, C, D): ")).upper()


if tipoapt == "A":
    valord = 150
elif tipoapt == "B":
    valord = 100
elif tipoapt == "C":
    valord = 75
elif tipoapt == "D":
    valord = 50
else:
    print("Tipo de apartamento inexistente!")
    sys.exit()

diarias = int(input("Quantas diárias o hospede adquiriu? "))
consumo = int(input("Qual foi o consumo do hóspede em reais (R$)? "))   

valortotal = valord * diarias
subtotal = valortotal + consumo
taxa = subtotal * 0.10
totalgeral = subtotal + taxa

print(f"\nNome do hóspede: {name}")
print(f"Tipo de apartamento: {tipoapt}")
print(f"Quantidade de diárias: {diarias}")
print(f"Valor da diária: {valord}R$")
print(f"Valor total das diárias: {valortotal}R$")
print(f"Valor consumido pelo hóspede: {consumo}R$")
print(f"Subtotal (consumo do hóspede + o valor total das diárias): {subtotal}R$")
print(f"Taxa de serviço (10%): {taxa}R$")
print(f"Valor total final: {totalgeral}R$")

