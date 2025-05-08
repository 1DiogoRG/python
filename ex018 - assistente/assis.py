import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import pyautogui
import time

voz = pyttsx3.init()
voz.setProperty('rate', 180)
voz.setProperty('voice', 'brazil')

def falar(mensagem):
    print("🟢 Assistente:", mensagem)
    voz.say(mensagem)
    voz.runAndWait()

def ouvir_comando():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as mic:
        print("🎤 Ouvindo você...")
        reconhecedor.adjust_for_ambient_noise(mic)
        audio = reconhecedor.listen(mic)

        try:
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print("🔵 Você:", comando)
            return comando.lower()
        except sr.UnknownValueError:
            falar("Desculpe, não entendi o que você disse.")
        except sr.RequestError:
            falar("Erro ao conectar com o serviço de voz.")
        return ""

def previsão_tempo():
    try:
        resposta = requests.get("https://wttr.in/?format=3")
        if resposta.status_code == 200:
            falar(f"Previsão do tempo: {resposta.text}")
        else:
            falar("Não consegui obter a previsão do tempo.")
    except:
        falar("Erro ao acessar o serviço de clima.")

def contar_piada():
    piadas = [
        "Por que o computador foi ao médico? Porque ele estava com um vírus!",
        "Qual é o cúmulo da distração? Tentar afogar um peixe.",
        "Por que o jacaré tirou o filho da escola? Porque ele réptil de ano!"
    ]
    import random
    falar(random.choice(piadas))

def anotar():
    falar("O que você quer anotar?")
    texto = ouvir_comando()
    if texto:
        with open("anotacoes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(texto + "\n")
        falar("Anotação salva com sucesso.")

def tocar_musica():
    falar("Qual música você quer ouvir?")
    musica = ouvir_comando()
    if musica:
        url = f"https://www.youtube.com/results?search_query={musica}"
        webbrowser.open(url)
        falar(f"Buscando {musica} no YouTube.")
        time.sleep(3)
        pyautogui.press("tab")  # Navega e simula clique (opcional)
        pyautogui.press("enter")

def assistente_voz():
    falar("Olá! Eu sou sua assistente de voz. O que você quer fazer hoje?")

    while True:
        comando = ouvir_comando()

        if "sair" in comando or "encerrar" in comando or "tchau" in comando:
            falar("Até logo! Foi bom falar com você.")
            break
        elif "seu nome" in comando:
            falar("Eu ainda não tenho um nome... Que tal você me dar um?")
        elif "que horas são" in comando or "me diga as horas" in comando:
            agora = datetime.datetime.now().strftime("%H:%M")
            falar(f"Agora são {agora}.")
        elif "pesquise por" in comando:
            termo = comando.replace("pesquise por", "").strip()
            url = f"https://www.google.com/search?q={termo}"
            falar(f"Pesquisando por {termo} no Google.")
            webbrowser.open(url)
        elif "abrir o youtube" in comando:
            falar("Abrindo o YouTube pra você.")
            webbrowser.open("https://www.youtube.com")
        elif "como você está" in comando:
            falar("Estou ótima! Obrigada por perguntar.")
        elif "previsão do tempo" in comando or "tempo hoje" in comando:
            previsão_tempo()
        elif "conte uma piada" in comando or "me faça rir" in comando:
            contar_piada()
        elif "anotar" in comando or "criar anotação" in comando:
            anotar()
        elif "tocar música" in comando or "ouvir música" in comando:
            tocar_musica()
        elif comando:
            falar("Desculpe, ainda não aprendi esse comando.")

assistente_voz()
