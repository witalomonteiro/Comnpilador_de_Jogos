import random

def jogar():
    print("\n***************************************")
    print("***** Bem-Vindo ao Jogo da Forca ******")
    print("***************************************")

    palavras = carregar_palavras("palavras.txt")
    palavra_secreta = sortear_palavra(palavras)
    palavra_dica = criar_dica(palavra_secreta)
    solicitar_letra_palpite(palavra_secreta, palavra_dica)

# Functions

def carregar_palavras (nome_arquivo):
    palavras = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().lower())
    return palavras

def sortear_palavra(palavras):
    random.seed()
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def criar_dica(palavra_secreta):
    palavra_dica = len(palavra_secreta) * "-"
    return palavra_dica

def solicitar_letra_palpite(palavra_secreta, palavra_dica):
    tentativas = 3
    print("\nDica: Frutas")
    for rodada in range(1, tentativas + 1):
        print(f"\nTentativa {rodada} de {tentativas}")
        # print(palavra_secreta)
        print(f"Palavra Secreta: {palavra_dica}")
        letra_palpite = input("Digite seu palpite: ").strip().lower()

        palavra_dica = validar_letra_palpite(palavra_secreta, palavra_dica, letra_palpite)

    validar_palavra_secreta(palavra_secreta, palavra_dica)

def validar_letra_palpite(palavra_secreta, palavra_dica, letra_palpite):
    if letra_palpite in palavra_secreta:
        palavra_dica = list(palavra_dica)
        for id, letra in enumerate(palavra_secreta):
            if letra_palpite == letra:
                # print(id)
                palavra_dica[id] = letra_palpite
        palavra_dica = "".join(palavra_dica)
    else:
        print(f"Letra não encontrada!")
    return palavra_dica
def validar_palavra_secreta(palavra_secreta, palavra_dica):
    palavra_palpite = input(f"\nQual é a palavra secreta '{palavra_dica}' ? ").strip().lower()
    if palavra_palpite == palavra_secreta:
        print("Parabéns! Você Acertou!")
    else:
        print("Errou! Fim de Jogo!")

if (__name__ == "__main__"):
    jogar()