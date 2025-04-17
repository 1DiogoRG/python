def cadastro_usuario():
    print("Bem-vindo ao cadastro de nossa loja")

    nome = input("digite seu nome: ")
    
    email = input("digite seu e-mail: ")

    senha = input("digite sua senha: ")
    confirma_senha = input("confirme sua senha: ")

    while senha != confirma_senha:
        print("SENHA INVALÍDA. Tente novamente")
        senha = input("Digite sua senha: ")
        confirma_senha = input("confirme sua senha: ")

    idade = int(input("digite a sua idade: "))

    if idade < 18:
        print("só maiores de 18 anos ou acima podem se cadastrar")
        return
    
    data_nascimento = input("digite sua data de nascimento (DD/MM/AAAA): ")
    telefone = input("digite seu numero de telefone: ")

    cpf = input("digite seu numero de cpf: ")

    while len(cpf) != 11 or not cpf.isdigit():
        print("CPD INVALÍDO, só podem ter 11 digitos")
        cpf = input("digite seu cpf: ")

    print("\ncadastro realizado com sucesso! aqui seus dados:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Idade: {idade}")
    print(f"Data de nascimento: {data_nascimento}")
    print(f"Telefone: {telefone}")
    print(f"CPF: {cpf}")

cadastro_usuario()