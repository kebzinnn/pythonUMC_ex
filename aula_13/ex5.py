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