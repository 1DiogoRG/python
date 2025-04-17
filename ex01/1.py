def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Não é possível dividir por zero."

def menu():
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def calculadora():
    while True:
        menu() 
        try:
            opcao = int(input("Digite o número da operação desejada (1/2/3/4): "))
            
            if opcao not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == 1:
                resultado = soma(num1, num2)
                print(f"O resultado da soma é: {resultado}")
            elif opcao == 2:
                resultado = subtracao(num1, num2)
                print(f"O resultado da subtração é: {resultado}")
            elif opcao == 3:
                resultado = multiplicacao(num1, num2)
                print(f"O resultado da multiplicação é: {resultado}")
            elif opcao == 4:
                resultado = divisao(num1, num2)
                print(f"O resultado da divisão é: {resultado}")

            continuar = input("Deseja realizar outra operação? (s/n): ")
            if continuar.lower() != 's':
                print("Obrigado por usar a calculadora!")
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

calculadora()
