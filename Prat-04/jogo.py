import random

# Crie um jogo onde cada usuário escolhe um número (1 a 6) 
# e o programa gera de forma aleatória um número de 1 a 6 (simulando um dado). 
# O usuário que acertar o número que foi sorteado vence. O programa deve validar 
# as escolhas impedindo que dois usuários diferentes escolham o mesmo número.

print(f"O jogo de hoje e advinhar o numero do dado. O JOGO consiste em adivinhar o numero que sera sorteado entre 1 a 6 pelo dado.")
print(f"Consoante o numero de jogadores, cada um deles vai dar o seu palpite e tentar adivinhar o numero atraves da sua sorte.")
print(f"Boa sorte e divirta-sse.")
print(f" ")

opcao = int(input("Digite o número de jogadores (Minimo: 2 e Maximo: 5): "))
def jogar_dado():
    return random.randint(1, 6)


if opcao == 2:
    print(f" ")
    print(f"Numeros Validos: 1, 2, 3, 4, 5 e 6")
    p1 = int(input("Insira o seu palpite Player 1: "))
    p2 = int(input("Insira o seu palpite Player 2: "))

    dado = jogar_dado()
    print(f"O número sorteado foi {dado}")

    if p1 == dado and p2 == dado:
        print("Empate")
    elif p1 == dado:
        print("Vencedor: Player 1")
    elif p2 == dado:
        print("Vencedor: Player 2")
    else:
        print("Ninguem venceu")


elif opcao == 3:
    print(f" ")
    print(f"Numeros Validos: 1, 2, 3, 4, 5 e 6")
    p1 = int(input("Insira o seu palpite Player 1: "))
    p2 = int(input("Insira o seu palpite Player 2: "))
    p3 = int(input("Insira o seu palpite Player 3: "))

    dado = jogar_dado()
    print(f"O número sorteado foi {dado}")

    if p1 == dado and p2 == dado and p3 == dado:
        print("Empate")
    elif p1 == dado:
        print("Vencedor: Player 1")
    elif p2 == dado:
        print("Vencedor: Player 2")
    elif p3 == dado:
        print("Vencedor: Player 3")
    else:
        print("Ninguem venceu")


elif opcao == 4:
    print(f" ")
    print(f"Numeros Validos: 1, 2, 3, 4, 5 e 6")
    p1 = int(input("Insira o seu palpite Player 1: "))
    p2 = int(input("Insira o seu palpite Player 2: "))
    p3 = int(input("Insira o seu palpite Player 3: "))
    p4 = int(input("Insira o seu palpite Player 4: "))

    dado = jogar_dado()
    print(f"O número sorteado foi {dado}")

    if p1 == dado and p2 == dado and p3 == dado and p4 == dado:
        print("Empate")
    elif p1 == dado:
        print("Vencedor: Player 1")
    elif p2 == dado:
        print("Vencedor: Player 2")
    elif p3 == dado:
        print("Vencedor: Player 3")
    elif p4 == dado:
        print("Vencedor: Player 4")
    else:
        print("Ninguem venceu")



elif opcao == 5:
    print(f" ")
    print(f"Numeros Validos: 1, 2, 3, 4, 5 e 6")
    p1 = int(input("Insira o seu palpite Player 1: "))
    p2 = int(input("Insira o seu palpite Player 2: "))
    p3 = int(input("Insira o seu palpite Player 3: "))
    p4 = int(input("Insira o seu palpite Player 4: "))
    p5 = int(input("Insira o seu palpite Player 5: "))

    dado = jogar_dado()
    print(f"O número sorteado foi {dado}")

    if p1 == dado and p2 == dado and p3 == dado and p4 == dado and p5 == dado:
        print("Empate")
    elif p1 == dado:
        print("Vencedor: Player 1")
    elif p2 == dado:
        print("Vencedor: Player 2")
    elif p3 == dado:
        print("Vencedor: Player 3")
    elif p4 == dado:
        print("Vencedor: Player 4")
    elif p5 == dado:
        print("Vencedor: Player 5")
    else:
        print("Ninguem venceu")

else:
    print("Erro. So pode ter de 2 a 5 jogadores")
