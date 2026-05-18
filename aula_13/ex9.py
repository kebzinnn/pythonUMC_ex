# 9) Elaborar um programa que contém uma lista com 15 elementos. Essa lista deve
# ser preenchida pelo usuário, porém não deve conter valores repetidos. Exibir
# no final a lista.

lista = []

while len(lista) < 15:
    x = int(input("Digite um valor: "))
    
    if x not in lista:
        lista.append(x)
    else:    
        print("Tente novamente:")
        

print(lista)