#calculadora de taxa de consumo

km = int(input("Digite a distância percorrida em KM: "))
gasolina = int(input("Digite a quantidade de litros de gasolina consumido: "))

taxa = gasolina / km
print(f"a taxa de consumo é de {taxa}L/KM")