import os
import json

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def mostrar_menu():
    print("\n===== TaskMaster 3000 =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Excluir tarefa")
    print("5 - Buscar tarefa por palavra")
    print("6 - Sair")
    print("===========================\n")

def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição: ")
    prioridade = input("Prioridade (baixa/média/alta): ").lower()
    nova = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    print("\n📋 Suas Tarefas:")
    for idx, t in enumerate(tarefas, start=1):
        status = "✅" if t["concluida"] else "❌"
        print(f"{idx}. [{status}] {t['titulo']} ({t['prioridade']})")
        print(f"   ↪ {t['descricao']}")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("✔️ Tarefa marcada como concluída.")
        else:
            print("❗ Número inválido.")
    except ValueError:
        print("❗ Entrada inválida.")

def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a excluir: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print(f"🗑️ Tarefa '{removida['titulo']}' excluída.")
        else:
            print("❗ Número inválido.")
    except ValueError:
        print("❗ Entrada inválida.")

def buscar_tarefa(tarefas):
    termo = input("Digite uma palavra-chave para buscar: ").lower()
    resultados = [t for t in tarefas if termo in t["titulo"].lower() or termo in t["descricao"].lower()]
    if resultados:
        print(f"\n🔍 Resultados para '{termo}':")
        for idx, t in enumerate(resultados, start=1):
            status = "✅" if t["concluida"] else "❌"
            print(f"{idx}. [{status}] {t['titulo']} ({t['prioridade']})")
            print(f"   ↪ {t['descricao']}")
    else:
        print("🔎 Nenhuma tarefa encontrada com esse termo.")

def main():
    tarefas = carregar_tarefas()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "5":
            buscar_tarefa(tarefas)
        elif opcao == "6":
            print("👋 Saindo do TaskMaster 3000. Até logo!")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
