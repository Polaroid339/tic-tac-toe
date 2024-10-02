import os

malha = [
    ["     ", "     ", "     "],
    ["     ", "     ", "     "],
    ["     ", "     ", "     "]
]

player1 = "  X  "
player2 = "  O  "

while True:
    print("    1       2       3")
    print(f"1 {malha[0][0]} | {malha[0][1]} | {malha[0][2]} ")
    print("-" * 25)
    print(f"2 {malha[1][0]} | {malha[1][1]} | {malha[1][2]} ")
    print("-" * 25)
    print(f"3 {malha[2][0]} | {malha[2][1]} | {malha[2][2]} \n")
    print("Jogador 1\n")

    while True:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        try:
            if linha-1 >= 4 or coluna-1 >= 4:
                print("Localização inválida")
            else:
                if malha[linha-1][coluna-1] == "     ":
                    malha[linha-1][coluna-1] = player1
                    os.system('cls')
                    break
                else:
                    print("Localização já prenchida\n")
        except ValueError:
            print("Caracter inválido")

    print("    1       2       3")
    print(f"1 {malha[0][0]} | {malha[0][1]} | {malha[0][2]} ")
    print("-" * 25)
    print(f"2 {malha[1][0]} | {malha[1][1]} | {malha[1][2]} ")
    print("-" * 25)
    print(f"3 {malha[2][0]} | {malha[2][1]} | {malha[2][2]} \n")
    print("Jogador 2\n")

    while True:
        linha2 = int(input("Digite a linha: "))
        coluna2 = int(input("Digite a coluna: "))
        try:
            if linha-1 >= 4 or coluna-1 >= 4:
                print("Localização inválida")
            else:
                if malha[linha2 - 1][coluna2 - 1] == "     ":
                    malha[linha2 - 1][coluna2 - 1] = player2
                    os.system('cls')
                    break
                else:
                    print("Localização já prenchida\n")
        except ValueError:
            print("Caracter inválido")
