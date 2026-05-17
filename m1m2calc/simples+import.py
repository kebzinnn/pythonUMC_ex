from comfuncao import obternota
import comfuncao

#calcula a média de notas usando M1 e M2 da UMC com conceitos básicos

materia = int(input("Escolha a matéria: \n Software Básico = 1 \n Redes e Seguranca = 2 \n"))


if materia == 1:
    print("Você selecionou Software Básico. \n")
elif materia == 2:
    print("Você selecionou Redes e Segurança. \n")
else:
    print("Matéria inválida. \n")

m1 = obternota("M1") #from lib import var
m2 = comfuncao.obternota("M2") #import lib

mfinal = (m1 + (m2 * 2)) / 3
print(f"Sua média final é {mfinal}")