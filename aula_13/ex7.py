# 7) Elaborar um programa em que o usuário deva inserir várias temperaturas. Todas as
# temperaturas precisam ser armazenadas em uma lista. Caso o usuário insira um número
# menor que zero (0) o programa finaliza a inserção de números. Logo em seguida, o
# programa deve acessar a lista gerada e classificar cada temperatura inserida.
# Classifique cada temperatura como: "Frio" (<10°C), "Agradável" (entre 10°C e 30°C),
# "Quente" (>30°C). O programa deve ignorar valores fora de valor plausível (acima
# de 60°C). Exiba a quantidade de ocorrências em cada categoria.
lista = []

while True:
    num = int(input("Digite uma temperatura: "))
    if num < 0:
        break
    if num < 60:
        lista.append(num)


frio = 0
agrad = 0
calor = 0

for temp in lista: #for i in range(len(lista)):
                        #temp = lista[i]
    if temp < 10:
        frio += 1
    elif temp <= 30:
        agrad += 1
    else:
        calor += 1

print(f"Frio: {frio}x")
print(f"Agradavel: {agrad}x")
print(f"Calor: {calor}x")