peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))
imc = peso / altura**2

if imc < 18.5:
    result = "Abaixo do peso"
elif imc < 25:
    result = "Peso normal"
elif imc < 30:
    result = "Sobrepeso"
else:
    result = "Obesidade"

print(f"IMC : {imc:.2f} | situação: {result}")