def form_aluno():
    print("Preencha seu formulário")

    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade <= 15:
                print("Você não pode continuar com o formulário.")
                break  # Encerra a função caso a idade seja menor ou igual a 15
            else:
                print("\nContinuando...\n")
                break  # Sai do loop se a idade for válida
        except ValueError:
            print("Por favor, digite uma idade válida (número).")

    if idade <= 15:
        return  # Encerra a função se não puder continuar

    escola = input("Digite o nome da escola: ")

    print("\nTipo de especialista")
    print("1 - Front-end")
    print("2 - Back-end")
    print("3 - Fullstack")

    opcaoEPCL = input("Digite o número da sua especialidade: ")
    if opcaoEPCL == "1":
        especialidade = "Front-end"
        print("Hmmm... Front-end, legal!")
    elif opcaoEPCL == "2":
        especialidade = "Back-end"
        print("Hmmm... Back-end, legal!")
    elif opcaoEPCL == "3":
        especialidade = "Fullstack"
        print("Hmmm... Fullstack, legal!")
    else:
        especialidade = "Especialidade inválida"
        print("ERRO! ESSA OPÇÃO NÃO EXISTE")

    print("\n--- Seus Dados ---")
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Idade: {idade}")
    print(f"Escola: {escola}")
    print(f"Você escolheu: {especialidade}")

form_aluno()
