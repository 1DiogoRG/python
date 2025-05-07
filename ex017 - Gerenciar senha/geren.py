import random
import string

def gerar_senha(total = 12):
    caract = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caract) for _ in range(total))

print("Sua senha gerada:", gerar_senha())