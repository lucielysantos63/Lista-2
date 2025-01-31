lista = []

while True:
    num = input("Digite um número (ou 'fim' para terminar): ")
    if num.lower() == 'fim':
        break
    
    num = int(num)
    i = 0
    while i < len(lista) and lista[i] < num:
        i += 1
    lista.insert(i, num)

print("Lista ordenada:", lista)