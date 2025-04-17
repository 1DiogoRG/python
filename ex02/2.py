print("olá, o qual tecnico você gostaria de aprender?")
print("A - Administração")
print("B - Desenvolvimento de sistemas")
print("C - Agropecuária")
print("S - Sair")
opcao = input("\ninsira umas das 3 opções ou nenhuma: ")
if opcao == "a":
    print("hmmm um tencico em Administração, boa escolha")
    nome = input("Ta esperando o que? diga seu nome já!: ")
    print(f"Seja muito bem-vindo {nome} o mais novo tecnico em Administração")
elif opcao == "b":
    print("hmmm um tecnico em Desenvolvimento de sistemas, boa escolha")
    nome = input("Ta esperando o que? diga seu nome já!: ")
    print(f"Seja muito bem-vindo {nome} o mais novo tecnico em Desenvolvimento de sistemas")    
elif opcao == "c":
    print("hmmm um recnico em Agropecuária, boa escolha")
    nome = input("Ta esperando o que? diga seu nome já!: ")
    print(f"Seja muito bem-vindo {nome} o mais novo tecnico em Agropecuária")
elif opcao == "s":
    print("aaah que pena cara, então ta bom nenhuma das 3 opções te agradou :(")
else:
    print("ERRRO, OPÇÃO INCORRETA. TENTE DE NOVO!!")