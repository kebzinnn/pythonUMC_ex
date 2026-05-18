'''
# Exercícios Lista - aula 13

# 1) Elaborar um programa que contenha uma lista com 16 elementos em que o usuário
# deve preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário
# que digite dois números. Esses números devem corresponder a posições na lista
# (caso contrário solicite um novo valor). Após inserir os dois números o programa
# deve exibir a soma dos elementos das duas posições da lista.
lista = []

for i in range(16):
    a = float(input(f"Digite o {i + 1}º valor: "))
    lista.append(a)

    soma = 0

for i in range(2):
    b = int(input(f"Digite o {i + 1}º número (0 - {len(lista) - 1})"))

    if 0 <= b <= len(lista) - 1:
        soma += lista[b]
    else:
        print(f"Digite um número entre 0 a {len(lista) - 1}")

print(f"soma = {soma}")


# 2) Elaborar um programa em que o usuário deva preencher uma lista com 30 números.
# Após o preenchimento o programa deve calcular a média dos números inseridos. Logo
# em seguida, o programa deve salvar em outra lista somente os números que são
# maiores que a média. Exibir no final a lista dos números maiores que a média.

lista = []

divisor = 0
for i in range(30):
    num = int(input(f"aloque uma posição ao índice {i}: "))
    lista.append(num)

    dividendo = sum(lista)
    divisor += 1

media = dividendo / divisor


lista2 = lista[:]
for numero in lista:
    if numero < media:
       lista2.remove(numero)

print(f"soma de todos os indices:", dividendo)
print(f"quantidade de números a ser dividido: ", divisor)
print(f"resultado da media: ", media)


print(f"valores a cima de {int(media)} arrendondo = {media:.0f}: ", lista2)


# 3) Elaborar um programa que dada uma lista com 15 números inteiros (inseridos
# pelo usuário), o programa deve a partir desta lista criar uma nova lista seguindo
# as seguintes regras: para números pares deve armazene o seu quadrado; se forem
# ímpares, armazene o seu cubo. Ao final, exiba a nova lista ordenada em ordem
# crescente.

lista = []

for i in range(15):
    num = int(input(f"Digite o indice {i}: "))
    lista.append(num)

lista2 = []

for i in lista:
    if (i % 2) == 0:
        lista2.append(i ** 2)
    else:
        lista2.append(i ** 3)

pares = []
impares = []

for i in lista:
    if (i % 2) == 0:
        pares.append(i ** 2)
    else:
        impares.append(i ** 3)

lista2.sort()   
print(lista2)
print(f"números pares: {pares}")
print(f"números impares: {impares}")


# 4) Elaborar um programa para uma loja que possui uma lista contendo a quantidade
# de itens em estoque para diversos produtos. Crie um programa que o usuário deva
# preencher o nome dos produtos e quantidade deste produto (uma lista para o nome
# e uma lista para quantidade). Classifique cada item como: "Estoque crítico"
# (quantidade menor que 5) ou "Estoque baixo" (entre 5 e 10) ou "Estoque normal"
# (acima de 10). Gere uma nova lista contendo apenas os produtos com estoque
# crítico. Exiba essa lista ao final.

nomel = []
qtdl = []
critico = []
baixo = []
normal = []
for i in range(3):
    nome = str(input(f"Digite o nome para o {i + 1}º produto: "))
    nomel.append(nome)
    qtd = int(input(f"Digite a quantidade para o {nome}: "))
    qtdl.append(qtd)

#for i in range(len(qtdl)):
    #qtd = qtdl[i]
    #nome = nomel[i]
produtos_ordenados = sorted(zip(qtdl, nomel)) #sorted deixa em ordem crescente e zip agrupa as duas listas

for qtd, nome in produtos_ordenados:
    formatacao = f"{nome} ({qtd})"

    if qtd < 5:
        critico.append(formatacao)
    elif qtd <= 10:
        baixo.append(formatacao)
    else:
        normal.append(formatacao)

print("critico: ", critico)
print("baixo: ", baixo)
print("normal:", normal)

# 5) Elaborar um programa que considere duas listas: uma com nomes de usuários e outra com
# suas respectivas senhas. Desenvolva um programa que solicite ao usuário login e senha. O
# programa deve permitir no máximo 3 tentativas. Informe se o acesso foi concedido ou se a
# conta foi bloqueada após as tentativas.

#com False/True
usuario = ["kleber1", "kleber2", "kleber3"]
senha = ["123", "456", "789"]

for tentativa in range(3):
    n = input("Digite seu nome de usuario: ")
    s = input("Digite sua senha: ")

    logado = False

    for i in range(len(usuario)):
        if n == usuario[i] and s == senha[i]:
            logado = True
            break

    if logado == True:
        print("Login confirmado")
        break
    else:
        print("tente novamente")
else:
    print("tentativas acabou")

#com list(zip(*lista1*, *lista2*))
usuario = ["kleber1", "kleber2", "kleber3"]
senha = ["123", "456", "789"]

logins = list(zip(usuario, senha))

for i in range(3):
    n = input("Digite seu nome de usuario: ")
    s = input("Digite sua senha: ")
    
    if (n, s) in logins:
        print("Login confirmado")
        break
    else:
        print(f"tente novamente, tentativa {i + 1} de 3")
else:
    print("tentativas acabou")


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

# 8) Elaborar um programa que o usuário deva preencher uma lista com 20 números
# inteiros. Após preencher a lista o programa deve verificar para cada número, se
# ele é primo ou não. O programa deve armazenar apenas os números primos em uma
# nova lista. Exiba a lista de primos e a quantidade encontrada.

lista = []
primosl = []

for i in range(20):
    num = int(input(f"Digite o {i + 1}º número: "))
    lista.append(num)

for num in lista:
    primo = True

    if num <= 1:
        primo = False
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                primo = False
                break

    if primo == True:
        primosl.append(num)

print(f"numeros primos: {primosl}, {len(primosl)}x")


# 9) Elaborar um programa que contém uma lista com 15 elementos. Essa lista deve
# ser preenchida pelo usuário, porém não deve conter valores repetidos. Exibir
# no final a lista.

lista = []

for i in range(15):
    x = int(input("Digite um valor: "))
    lista.append(x)

listasemrep = set(lista)
print(listasemrep)


lista = []

while len(lista) < 15:
    x = int(input("Digite um valor: "))
    
    if x not in lista:
        lista.append(x)
    else:    
        print("Tente novamente:")
        

print(lista)
'''