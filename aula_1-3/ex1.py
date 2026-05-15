#calculadora de dolares para reais
cotacao = float(input("Digite a cotação atual do dólar: "))
qtd = float(input("Digite quantos dólares você possui: "))

reais = qtd * cotacao
print(f"Você tem {reais}R$")