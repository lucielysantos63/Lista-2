numeros = []
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

print("Lista resultante:", numeros)