# Elaborar um algoritmo que deve ler N números. 
# Caso o usuário digite zero (0), o programa deve exibir a somatória e a média dos valores inseridos.

contador = 0
soma = 0

while True:
    
    num = float(input("Digite um numero: "))
    
    if num == 0: 
        break

    contador += 1
    soma += num

if contador > 0:
    media = soma / contador

    print(f"Soma = {soma}")
    print(f"Média = {media}")

else:
    print("Não há nenhum número")