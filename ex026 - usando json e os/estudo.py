import json
import os

# Onde quero salvar os dados do usuário gerando um arquivo 'dados.json':
ARQUIVO = "dados.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as a:
            return json.load(a)
    except:
        return []

# Salvo o registro no arquivo JSON
def salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as a:
        json.dump(lista, a, indent=4, ensure_ascii=False)

# Vai coletar os dado do usuário
def add_usuario():
    nome = input("\nNome: ").strip()
    sobrenome = input("Sobrenome: ").strip()

    while True:
        idade = input("Idade: ").strip()
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print("Erro: apenas números")

    sexo = input("Sexo: ").strip()
    profissao = input("Profissão: ").strip()
    email = input("E-mail: ").strip()
    escola = input("Escola: ").strip()
    turma = input("Turma: ").strip()
    turno = input("Turno: ").strip()

    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "sexo": sexo,
        "profissão": profissao,
        "e-mail": email,
        "escola": escola,
        "turma": turma,
        "turno": turno
    }

# Mostra todos os registros salvos
def listar(lista):
    if not lista:
        print("Nenhum registro")
        return
    
    for i, item in enumerate(lista, start=1):
        print(f"#{i} | {item['nome']} - {item['idade']} anos")

# Parte principal do código pra executar
def menu():
    registros = carregar()
    while True:
        print("\n== MENU ==")
        print("1) - Adicionar Usuário")
        print("2) - Listar Usuários")
        print("3) - Sair")

        opcao = input("Escolha uma das opções: ").strip()
        if opcao == '1':
            novo = add_usuario()
            registros.append(novo)
            salvar(registros)
            print("Registro salvo com sucesso")
        elif opcao == '2':
            listar(registros)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Ainda não existe essa opção")

if __name__ == "__main__":
    menu()