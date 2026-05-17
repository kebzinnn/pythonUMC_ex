
lista = [1, -2, -37, 23, 11, 2, 5, 4, 6, 6, 7, 8]

lista.sort()
lista.reverse()

print(f"lista 1: \n{lista}\n")

a = sum(lista)
print("soma:", a)
b = max(lista)
print("Maior valor:", b)
c = min(lista)
print("menor valor:", c)
d = len(lista)
print(f"quantidade de elementos: {d}")
print(f"qtd de indices: {d - 1}\n")

valor = [2, 4]
valor.extend([8, 1, 1, 1, 1])
x = valor.count(1)


y = lista.index(-37)
print(y)


valor.insert(3, "kleber")

print(f"{x}\n{valor}")

array = [1, 2, 3, 4]
array.pop(2)
print(array)

x = array.pop(0)
print(x)
print(array)


#texto = "www.eupoderiaterestudadomais.com"

#print(texto.split("."))
#print("13:15:45".split(":"))
#hora, minuto, segundo = "13:15:45".split(":")