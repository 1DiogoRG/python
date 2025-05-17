import random

palavras = [
    "python", "programador", "computador", "internet", "teclado",
    "algoritmo", "variavel", "inteligencia", "artificial", "desenvolvedor"
]

def escolher_palavra():
    return random.choice(palavras).lower()

def mostrar_palavra(palavra, letras_adivinhadas):
    return ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])

def jogar_forca():
    print("🎮 Bem-vindo ao Jogo da Forca!")
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6

    while True:
        print("\nPalavra:", mostrar_palavra(palavra_secreta, letras_adivinhadas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas UMA letra válida.")
            continue

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue

        letras_adivinhadas.add(letra)

        if letra not in palavra_secreta:
            tentativas_restantes -= 1
            print(f"A letra '{letra}' não está na palavra.")

        if all(letra in letras_adivinhadas for letra in palavra_secreta):
            print("\nParabéns! Você acertou a palavra:", palavra_secreta)
            break

        if tentativas_restantes == 0:
            print("\nFim de jogo! A palavra era:", palavra_secreta)
            break

if __name__ == "__main__":
    jogar_forca()
