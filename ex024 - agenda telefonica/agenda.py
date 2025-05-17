import json

def carregar_agenda():
    try:
        with open("agenda.json", "r") as f:
            return json.load(f)
    except:
        return {}
    
def salvar_agenda(agenda):
    with open("agenda.json", "w") as f:
        json.dump(agenda, f, indent=4)

def menu():
    agenda = carregar_agenda()
    while True:
        print("[1] - Adicionar")
        print("[2] - Buscar")
        print("[3] - Listar")
        print("[4] - Sair")
        opcao = input("\nEscolha: ")
        if opcao == '1':
            nome = input("Nome: ")
            tel = input("Telefone: ")
            agenda[nome] = tel
            salvar_agenda(agenda)
        elif opcao == '2':
            nome = input("Buscar: ")
            print(f"{nome}: {agenda.get(nome, 'não encontrado')}")
        elif opcao == '3':
            for nome, tel in agenda.items():
                print(f"{nome}: {tel}")
        elif opcao == '4':
            break

menu()