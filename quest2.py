frutas = ['maça', 'uva', 'melancia', 'banana', 'manga']

nome_da_fruta = input("Digie o nome da fruta: ")
tamanho_da_lista = len(frutas)

for i in range(tamanho_da_lista):
    if frutas[i] == nome_da_fruta:
        print(f"A fruta {nome_da_fruta} está na lista")
        break
else:
    print(f"A fruta {nome_da_fruta} não está na lista")