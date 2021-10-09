import adivinhacao
import forca

def escolher_jogo():
    print("****************************************")
    print("*** Bem-Vindo ao Compilador de Jogos ***")
    print("****************************************")

    print("\n[1] Adivinhação  [2] Forca")
    opcao = int(input("Escolha seu jogo: "))

    if opcao == 1:
        adivinhacao.jogar()
    elif opcao == 2:
        forca.jogar()

if (__name__ == "__main__"):
    escolher_jogo()