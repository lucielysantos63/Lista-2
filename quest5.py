L = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

cidade = input("Digite o nome de uma cidade: ")

if cidade in L:
    print(f"A Cidade {cidade} está na lista")
else:
    print(f"A Cidade {cidade} não está na lista")