# 6) Elaborar um programa que dada uma lista com pontuações de jogadores, crie um
# programa que remova valores duplicados, ordene as pontuações em ordem decrescente,
# classifique os três primeiros colocados como "elite", classifique os demais como
# "amadores". Exiba o resultado.

lista = []

for i in range(10):

    pontuacao = int(input(f"Digite a pontuação do {i + 1}º jogador: "))
    if pontuacao not in lista:
        lista.append(pontuacao) 

lista.sort()
lista.reverse()

for i in range(len(lista)):
    pontos = lista[i]
    if i + 1 <= 3:
        print(f"{i + 1}º colocado é elite, com {pontos} pontos")
    else:
        print(f"{i + 1}º colocado é amador, com {pontos} pontos")