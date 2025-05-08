import json
import os

arquivo = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4)

def add_tarefa(tarefas):
    tarefa = input("Nova tarefa: ")
    tarefas.append({"tarefa": tarefa, "feito": False})
    salvar_tarefas(tarefas)

def listar_tarefas(tarefas):
    for i, t in enumerate(tarefas):
        status = "✔️" if t["feito"] else "❌"
        print(f"{i+1}. {t['tarefa']} [{status}]")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    i = int(input("Número da tarefa concluída: ")) - 1
    if 0 <= i < len(tarefas):
        tarefas[i]["feito"] = True
        salvar_tarefas(tarefas)

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n1. Listar\n2. adicionar\n3. Marcar concluída\n4. Sair")
        escolha = input("Escolha: ")
        if escolha == "1":
            listar_tarefas(tarefas)
        elif escolha == "2":
            add_tarefa(tarefas)
        elif escolha == "3":
            marcar_concluida(tarefas)
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

menu()
