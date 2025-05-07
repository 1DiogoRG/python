import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

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
        elif comando:
            falar("Desculpe, ainda não aprendi esse comando.")

assistente_voz()