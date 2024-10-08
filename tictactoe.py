import os
import sys

malha = [
    ["     ", "     ", "     "],
    ["     ", "     ", "     "],
    ["     ", "     ", "     "]
]

player1 = "  X  "
player2 = "  O  "


def checkwin(var):
    if malha[0][0] == malha[1][1] == malha[2][2] == var:
        print(f"O jogador {var.strip()} venceu")
        sys.exit()

    if malha[0][2] == malha[1][1] == malha[2][0] == var:
        print(f"O jogador {var.strip()} venceu")
        sys.exit()

    for x in range(3):
        if malha[x][0] == malha[x][1] == malha[x][2] == var:
            print(f"O jogador {var.strip()} venceu")
            sys.exit()

    for y in range(3):
        if malha[0][y] == malha[1][y] == malha[2][y] == var:
            print(f"O jogador {var.strip()} venceu")
            sys.exit()
    for z in malha:
        if "     " in z:
            return False

    print("O jogo empatou")
    sys.exit()


while True:
    print("    1       2       3")
    print(f"1 {malha[0][0]} | {malha[0][1]} | {malha[0][2]} ")
    print("-" * 25)
    print(f"2 {malha[1][0]} | {malha[1][1]} | {malha[1][2]} ")
    print("-" * 25)
    print(f"3 {malha[2][0]} | {malha[2][1]} | {malha[2][2]} \n")

    print("Jogador X\n")
    while True:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        try:
            if (linha) > 3 or (coluna) > 3:
                print("\nLocalização inválida\n")

            elif (linha) == 0 or (coluna) == 0:

                print("\nLocalização inválida\n")

            elif malha[linha-1][coluna-1] == "     ":
                malha[linha-1][coluna-1] = player1
                os.system('cls')
                break

            else:
                print("\nLocalização já preenchida\n")

        except ValueError:
            print("Caracter inválido")

    checkwin(player1)

    print("    1       2       3")
    print(f"1 {malha[0][0]} | {malha[0][1]} | {malha[0][2]} ")
    print("-" * 25)
    print(f"2 {malha[1][0]} | {malha[1][1]} | {malha[1][2]} ")
    print("-" * 25)
    print(f"3 {malha[2][0]} | {malha[2][1]} | {malha[2][2]} \n")

    print("Jogador O\n")
    while True:
        linha2 = int(input("Digite a linha: "))
        coluna2 = int(input("Digite a coluna: "))
        try:
            if (linha2) > 3 or (coluna2) > 3:
                print("\nLocalização inválida\n")

            elif (linha2) == 0 or (coluna2) == 0:

                print("\nLocalização inválida\n")

            elif malha[linha2-1][coluna2-1] == "     ":
                malha[linha2-1][coluna2-1] = player2
                os.system('cls')
                break

            else:
                print("\nLocalização já preenchida\n")

        except ValueError:
            print("Caracter inválido")

    checkwin(player2)
