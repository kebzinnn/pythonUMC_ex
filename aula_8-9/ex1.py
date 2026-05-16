# Elaborar um algoritmo que solicita varias temperaturas em graus Celsius. O programa termina quanto a temperatura inserida for menor que -5. 
# Para cada temperatura inserida, o programa deve convertê-la em graus Fahrenheit e mostra-la na tela.

while True:
    temperatura = float(input("Insira o valor em graus Celsius para converte-lá para graus Farenheit (valor mínimo: -5): "))

    if temperatura >= -5: 
        conversao = temperatura * (9/5) + 32
        print(f"A temperatura {temperatura}C equivale a {conversao}F")
    else:   
        break