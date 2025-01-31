lista_compras = []

while True:
    print("Menu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        item = input("Digite o item a adicionar: ")
        lista_compras.append(item)
        print("Item adicionado.")
    elif escolha == "2":

        item = input("Digite o item a remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido.")
        else:
            print("Item não encontrado na lista.")
    elif escolha == "3":
        print("Lista de compras:", lista_compras)
    elif escolha == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")