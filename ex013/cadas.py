# -> O usuário ira ter várias opções para escolher logo a baixo.
# -> Cada opção vai ser uma coisa diferente da outra.

def opcao_user():

    # aqui são as opções que tem no menu
    print("=-> Escolha uma Opção <-=")
    print("====== Menu Opções ==========")
    print("🤓 [1] -> Loja [✅]")
    print("🤓 [2] -> Escola [✅]")
    print("🤓 [3] -> Calculadora [✅]")
    print("🤓 [4] -> Ìmpar ou Par [✅]")
    print("🤓 [5] -> Conversor de Temperatura [✅]")
    print("🤓 [6] -> Real para Dolar [✅]")
    print("🤓 [7] -> Descobrir idade [✅]")
    print("🤓 [8] -> Sair [✅]")
    print("🤓 [9] -> Jogo de adivinhação [✅]")
    print("=============================")

    # onde o usuário escolhe a opção
    opcao = input("Qual opção deseja (1/2/3/4/5/6/7/8)? ")

    # Opção - 1
    if opcao == "1":
        print("===-- Loja --===")
        # pergunta seu nome
        nome = input("Digite seu nome: ")
        
        try:
            # pergunta sua idade
            idade = int(input("Digite sua idade: "))
        except ValueError:
            # aqui vai exebir uma mensagem de erro se não for número
            print("idade inválida")
            return

        # verfica se a idade é menor que 18
        if idade < 18:
            print(f"\n❌ {nome} você não pode se cadastrar nessa loja porque tem idade baixa ❌")
            return
        
        # se usuário tiver a idade o suficiente continuara o cadastro
        print("\nVamos continuar...")
        
        # pergunta a data de nascimneto
        data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        # pergunta o e-mail do usuário
        email = input("Coloque seu E-mail: ")

        # confirmação da senha
        while True:
            senha = input("🔒 Digite sua senha: ")
            confirma_senha = input("🔒 Confrirme sua senha: ")

            # se as senhas forem iguais continua sem problema
            if senha == confirma_senha:
                print(f"\n✅ Senha cadastrada com sucesso {nome}! ✅")
                break
            else:
                print(f"\n❌ As senhas não são as mesma {nome} ❌")
        
        # validação do CPF
        while True:
            cpf = input("Digite seu CPF (11 dígitos): ")

            # verifica se o CPF tem 11 números
            if len(cpf) == 11 and cpf.isdigit():
                print("CPF válido")
                break
            else:
                print("❌ CPF inválido. Não exatamente 11 dígitos ❌")

        # aqui vai mostrar os dados do usuário
        print("\n====================")
        print("===-- ✅ Seus dados ✅ --===")
        print(f"🧑‍🦰 Nome: {nome}")
        print(f"🧑‍🦳 Idade: {idade} anos")
        print(f"👶 Data de nascimento: {data_de_nascimento}")
        print(f"✉️ E-mail: {email}")
        print(f"🔒 Senha de usuário: {senha}")
        print(f"🤑 CPF: {cpf}")
        print("======================")

    # opção - 2
    elif opcao == "2":
        print("===-- Escola --===")
        # seu nome
        nome = input("Digite seu nome: ")

        try:
            idade = int(input("Digite sua idade: "))
        except ValueError:
            print("idade inválida")
            return
        
        # cadastro aceito
        print("\nCadastro realizado com sucesso")

        # mostrar os dados
        print("=======================")
        print("===-- Seus dados --===")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print("Feito o seu cadastro")
        print("=======================")
    
    # opção - 3
    elif opcao == "3":
        print("===-- Calculadora --===")
        try:
            num1 = float(input("Primeiro número: ")) # primeiro número
            operador = input("Escolha um operador (+, -, *, /): ") # escolhe qual operador
            num2 = float(input("Segundo número: ")) # segundo número

            if operador == "+": #soma
                resultado = num1 + num2
            elif operador == "-": # subtração
                resultado = num1 - num2
            elif operador == "*": # multiplicação
                resultado = num1 * num2
            elif operador == "/": # divisão
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("a divisão não pode ser por Zero")
                    return
            else:
                print("não tem esse Operador")

            print(f"O resultado é: {resultado}")
        except ValueError:
            print("Erro: inválido e use números")
        else:
            print("Opção inválida")
    
    # opção - 4
    elif opcao == "4": # verifica se número é par ou ímpar
        print("===-- Ímpar ou Par --===")
        numero = int(input("Digite um numero: "))

        if numero % 2 == 0:
            print(f"Número {numero} é Par")
        else:
            print(f"Número {numero} é Ímpar")

    # opção - 5
    elif opcao == "5": # conversor de temperatura
        print("===-- Conversor de Temperatura --===")
        escolha = input("Converter (1) Celsius para Fahrenheit ou (2) Fahrenheit para Celsius? ")

        try:
            temp = float(input("Digite a temperatura: "))
            if escolha == "1":
                print(f"{temp}°C = {(temp * 9/5) + 32}°F")
            elif escolha == "2":
                print(f"{temp}°F = {(temp - 32) * 5/9}°C")
            else:
                print("Escolha inválida")
        except ValueError:
            print("Temperatura inválida")
    
    # opção - 6
    elif opcao == "6": # conversor de Real para o Dolar
        print("===-- Real para Dolar --===")
        try:
            real = float(input("Quantos reais você tem (R$)? "))
            cotacao = float(input("Digite a cotação: "))
            dolar = real / cotacao
            print(f"R$ {real:.2f} equivale a US$ {dolar:.2f}")
        except ValueError:
            print("ERRO ensira apenas numeros")

    # opção - 7
    elif opcao == "7": # calcula a idade com base no ano do nascimento
        print("===-- Descobrir a idade --===")
        nome = input("Diga seu nome: ")
        ano_atual = int(input("Ano atual: "))
        ano_nasceu = int(input("Ano que nasceu: "))
        
        idade = ano_atual - ano_nasceu
        print(f"\n{nome} você nasceu em {ano_nasceu} e tem extamente: {idade} anos")

    elif opcao == "8":

        import random
        numeroSecreto = random.randint(1, 100)
        tentativa = -1
        print("Quero você tente advinhar o número de 1 e 100")

        while tentativa != numeroSecreto:
            tentativa = int(input("Qual seu palpite?👀 "))
            if tentativa < numeroSecreto:
                print("Muito baixo")
            elif tentativa > numeroSecreto:
                print("Muito alto")
            else:
                print("Você acertou")

    # opção - 9
    elif opcao == "9": # sair com confirmação
        print("===-- Sair --===")

        # loop até o usuário dar resposta válida
        while True:
            sair = input("Realmente que sair? digite 'sim' para voltar ou 'não' para encerrar: ").strip().lower()
            if sair == "sim":
                # ira voltar ao menu se no caso for 'sim'
                opcao_user()
                break
            elif sair == "não":
                # finaliza  oprograma se no caso for 'não'
                print("✅ Programa finalizado")
                exit()
            else:
                print("❌ Resposta inválida. É 'sim' ou 'não'")

opcao_user()