import random
numero_escolhido = [random.randint(1, 100)]

print("O programa escolheu um número.")

while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero_escolhido[0]:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Número errado! Tente novamente.")