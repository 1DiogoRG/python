import random
import time
import sys
from colorama import init, Fore
init(autoreset=True)

def digitar_mensagem(mensagem, atraso=0.04):
    for mmsg in mensagem:
        print(mmsg, end='', flush=True)
        time.sleep(atraso)
    print()

def bot_simples():
    digitar_mensagem("🤖  Olá! Eu sou um bot. Pode conversar comigo. (Digite 'sair' para encerrar)\n")

    while True:
        usuario = input("\nVocê: ").lower()

        if usuario == 'sair':
            digitar_mensagem("🤖 Bot: Tchau! Até a próxima!")
            break
        elif 'oi' in usuario or 'olá' in usuario:
            digitar_mensagem("🤖 Bot: Oi! Tudo bem com você?")
        elif 'tudo bem' in usuario:
            digitar_mensagem("🤖 Bot: Que bom! Eu também estou bem.")
        elif 'qual seu nome' in usuario:
            digitar_mensagem("🤖 Bot: Eu sou um bot feito em Python! Ainda não tenho nome 😅")
        elif 'quem criou você' in usuario:
            digitar_mensagem("🤖 Bot: Quem me criou foi Diogo Rodrigues 🤩")
        elif 'ajuda' in usuario:
            digitar_mensagem("🤖 Bot: Você pode me perguntar coisas simples como 'oi', 'tudo bem', ou 'qual seu nome'.")
        elif 'professor' in usuario:
            digitar_mensagem("🤖 Bot: Seus professores queridos, ⭐ Francisco e Márcio ⭐, eles dois são demais! É um privilégio aprender com mestres tão dedicados!")
            print(Fore.RED + "Hello World!")
            print(Fore.BLUE + "💵 Francisco e Márcio 💵")
            digitar_mensagem("public class Main{")
            digitar_mensagem("    public static void main(String[] args){")
            digitar_mensagem("        System.out.println('Hello World!')")
            digitar_mensagem("    }")
            digitar_mensagem("}")
            print(Fore.YELLOW + "#Para você Francisco")
        elif 'jogar' in usuario:
            digitar_mensagem("🤖 Bot: Que tal o jogo de adivinhação?")
            resposta = input("Você: ").lower()
            if 'não' in resposta:
                digitar_mensagem("🤖 Bot: Tá bom, vamos tentar outro jogo depois.")
                break
            elif 'vamos' in resposta or 'sim' in resposta:
                digitar_mensagem("🤖 Bot: Ebaaa! Vamos lá!")
                numero_secreto = random.randint(1, 100)
                tentativa = -1
                digitar_mensagem("🤖 Bot: Quero ver você adivinhar o número!")

                while tentativa != numero_secreto:
                    try:
                        tentativa = int(input("🤖 Bot: Diga seu palpite 👀: "))
                        if tentativa < numero_secreto:
                            digitar_mensagem("🤖 Bot: Muito baixo.")
                        elif tentativa > numero_secreto:
                            digitar_mensagem("🤖 Bot: Muito alto.")
                        else:
                            digitar_mensagem("🤖 Bot: Parabéns, você acertou! 🥳")
                    except ValueError:
                        digitar_mensagem("🤖 Bot: Digite um número válido!")

            elif 'outro' in resposta:
                digitar_mensagem("🤖 Bot: Vamos jogar Pedra, Papel e Tesoura!")
                resposta = input("Você: ").lower()
                if 'não' in resposta:
                    digitar_mensagem("🤖 Bot: Tá bom, vamos tentar outro jogo depois.")
                    break
                elif 'sim' in resposta or 'vamos' in resposta:
                    opcoes = ['pedra', 'papel', 'tesoura']
                    jogador = input("🤖 Bot: Escolha pedra, papel ou tesoura: ").lower()
                    if jogador not in opcoes:
                        digitar_mensagem("🤖 Bot: Escolha inválida")
                        continue
                    bot = random.choice(opcoes)
                    digitar_mensagem(f"🤖 Bot: Você escolheu {jogador}")
                    digitar_mensagem(f"🤖 Bot: Eu escolhi {bot}")
                    if jogador == bot:
                        digitar_mensagem("🤖 Bot: Empate!")
                    elif (jogador == 'pedra' and bot == 'tesoura') or \
                        (jogador == 'papel' and bot == 'pedra') or \
                        (jogador == 'tesoura' and bot == 'papel'):
                        digitar_mensagem("🤖 Bot: Você venceu!")
                    else:
                        digitar_mensagem("🤖 Bot: Você perdeu!")

        else:
            digitar_mensagem("🤖 Bot: Hmmm... não entendi. Pode tentar de outro jeito?")

bot_simples()
