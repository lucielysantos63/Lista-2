fila_espera = []

while True:
    
    print("Fila atual:", fila_espera)
    print("Opções:")
    print("1. Adicionar paciente à fila")
    print("2. Atender paciente")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_paciente = input("Digite o nome do paciente para adicionar à fila: ")
        fila_espera.append(nome_paciente)
    elif escolha == "2":
        
        if fila_espera:
            paciente_atendido = fila_espera.pop(0)
            print("Atendendo o paciente:", paciente_atendido)
        else:
            print("Fila vazia. Não há pacientes para atender.")
    elif escolha == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")