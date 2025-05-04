import random

def bot_simples():
    print("🤖 Olá! Eu sou um bot. Pode conversar comigo. (Digite 'sair' para encerrar)\n")

    while True:
        usuario = input("Você: ").lower()

        if usuario == 'sair':
            print("Bot: Tchau! Até a próxima!")
            break
        elif 'oi' in usuario or 'olá' in usuario:
            print("Bot: Oi! Tudo bem com você?")
        elif 'tudo bem' in usuario:
            print("Bot: Que bom! Eu também estou bem.")
        elif 'qual seu nome' in usuario:
            print("Bot: Eu sou um bot feito em Python! Ainda não tenho nome 😅")
        elif 'quem criou você' in usuario:
            print("Bot: Quem me criou foi Diogo Rodrigues 🤩")
        elif 'ajuda' in usuario:
            print("Bot: Você pode me perguntar coisas simples como 'oi', 'tudo bem', ou 'qual seu nome'.")
        elif 'jogar' in usuario:
            print("Bot: Que tal o jogo de adivinhação?")
            resposta = input("Você: ").lower()
            if 'não' in resposta:
                print("Bot: Tá bom, vamos tentar outro jogo depois.")
                break
            elif 'vamos' in resposta or 'sim' in resposta:
                print("Bot: Ebaaa! Vamos lá!")
                numero_secreto = random.randint(1, 100)
                tentativa = -1
                print("Bot: Quero ver você adivinhar o número!")

                while tentativa != numero_secreto:
                    try:
                        tentativa = int(input("Bot: Diga seu palpite 👀: "))
                        if tentativa < numero_secreto:
                            print("Bot: Muito baixo.")
                        elif tentativa > numero_secreto:
                            print("Bot: Muito alto.")
                        else:
                            print("Bot: Parabéns, você acertou! 🥳")
                    except ValueError:
                        print("Bot: Digite um número válido!")

            elif 'outro' in resposta:
                print("Bot: Vamos jogar Pedra, Papel e Tesoura!")
                resposta = input("Você: ").lower()
                if 'não' in resposta:
                    print("Bot: Tá bom, vamos tentar outro jogo depois.")
                    break
                elif 'sim' in resposta or 'vamos' in resposta:
                    opcoes = ['pedra', 'papel', 'tesoura']
                    jogador = input("Bot: Escolha pedra, papel ou tesoura: ").lower()
                    if jogador not in opcoes:
                        print("Bot: Escolha inválida")
                        continue
                    bot = random.choice(opcoes)
                    print(f"Bot: Você escolheu {jogador}")
                    print(f"Bot: Eu escolhi {bot}")
                    if jogador == bot:
                        print("Bot: Empate!")
                    elif (jogador == 'pedra' and bot == 'tesoura') or \
                        (jogador == 'papel' and bot == 'pedra') or \
                        (jogador == 'tesoura' and bot == 'papel'):
                        print("Bot: Você venceu!")
                    else:
                        print("Bot: Você perdeu!")

        else:
            print("Bot: Hmmm... não entendi. Pode tentar de outro jeito?")

bot_simples()
