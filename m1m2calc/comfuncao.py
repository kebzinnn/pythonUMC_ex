'''
def obternota(nomenota):

    nota = -1

    while nota > 10 or nota < 1:
        nota = float(input(f"Digite sua {nomenota}: "))
        if nota > 10:
            print("Nota máxima = 10")
        elif nota < 1:
            print("Nota mínima = 1")

m1 = obternota("M1")
m2 = obternota("M2")

media = (m1 + (m2 * 2)) / 3
print("media final é:", media)


            
'''
#biblioteca que servirá de import
def obternota(nomenota):

    while True:
        nota = float(input(f"Digite sua {nomenota}: "))

        if nota > 10:
            print("Nota máxima = 10")
        elif nota < 1:
            print("Nota mínima = 1")
        else:
            return nota


#arquivo que importará a biblioteca
m1 = obternota("M1")
m2 = obternota("M2")

media = (m1 + (m2 * 2)) / 3

print(f"A média final é {media:.3f}") #3 casas decimais pos ponto