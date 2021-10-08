
def jogar():
    print("***************************************")
    print("***** Bem-Vindo ao Jogo da Forca ******")
    print("***************************************")

    palavra_secreta = "banana"
    tentativas = 3

    while tentativas > 0:
        palpite = input("Digite seu palpite: ").strip()
        if palpite in palavra_secreta:
            for id, letra in enumerate(palavra_secreta):
                if palpite.upper() == letra.upper():
                    print(id)
        else:
            print("Palavra não encontrada!")
        tentativas -= 1

if (__name__ == "__main__"):
    jogar()