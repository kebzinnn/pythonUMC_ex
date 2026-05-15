# Elabore um algoritmo que calcule a soma de dois números quaisquer 
# e apresente na tela o resultado dessa soma. Caso a soma seja supe-
# rior a 30, indicar qual é o maior valor entre eles.

n1 = float(input("n1: "))
n2 = float(input("n2: "))

soma = n1 + n2

if soma < 30:
    print("soma: ", soma)
elif soma > 30:
    print("soma: ", soma)
    if n1 > n2:
        print("maior numero:", n1)
    elif n2 > n1:
        print("maior numero:", n2)
    

