print("Olá, qual cruso você quer seguir?")
print("a - Administração")
print("b - Desenvolvimento de sistemas")
print("c - Agropecuária")
print("s - Sair")

print("\ncoloque suas informações para seguir o progresso.")
nome = input("coloque seu nome: ")
idade = int(input("coloque sua idade: "))
if idade <= 14:
    print("você não pode fazer esse curso, volte mais tarde quando tiver a idade certa!")
elif idade <= 15:
    print("você tem a idade certa para fazer esse curso!")
    print("então vamos continuar com o progresso.")

opcao = input("\ndigite uma das opções acima: ")
if opcao == "a":
    print("hmmm um tencico em Administração, boa escolha")
    print(f"\nSeja muito bem-vindo {nome} o mais novo tecnico em Administração")
elif opcao == "b":
    print("hmmm um tecnico em Desenvolvimento de sistemas, boa escolha")
    print(f"\nSeja muito bem-vindo {nome} o mais novo tecnico em Desenvolvimento de sistemas")    
elif opcao == "c":
    print("hmmm um recnico em Agropecuária, boa escolha")
    print(f"\nSeja muito bem-vindo {nome} o mais novo tecnico em Agropecuária")
elif opcao == "s":
    print("\naaah que pena cara, então ta bom nenhuma das 3 opções te agradou :(")
else:
    print("\nERRRO, OPÇÃO INCORRETA. TENTE DE NOVO!!")