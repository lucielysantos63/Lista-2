lista_inicial = [1, 2, 3, 4, 5, 6]
print("Lista inicial:", lista_inicial)

print("Removendo números pares...")

for numero in lista_inicial[:]:
    if numero % 2 == 0:
        lista_inicial.remove(numero)

print("Lista resultante:", lista_inicial)