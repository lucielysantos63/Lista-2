lista_inicial = [1, 2, 3, 4, 5]
print("Lista inicial:", lista_inicial)

numero = int(input("Digite o número que deseja inserir: "))
posicao = int(input("Digite a posição onde deseja inserir: "))

lista_inicial.insert(posicao, numero)

print(f"Lista resultante:", lista_inicial)