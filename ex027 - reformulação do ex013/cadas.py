import json
import random
import sys
import os

def carregar_json(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def exibir_menu():
    print("=-> Escolha uma Opção <-=")
    print("====== Menu Opções ==========")
    print("🤓 [1] -> Loja")
    print("🤓 [2] -> Escola")
    print("🤓 [3] -> Calculadora")
    print("🤓 [4] -> Real para Dolar")
    print("🤓 [5] -> Jogo de adivinhação")
    print("🤓 [6] -> Sair")
    print("=============================")
    return input("Qual opção deseja (1/2/3/4/5/6)? ").strip()

def opcao_loja():
    print("===-- Loja --===")
    nome = input("Digite seu nome: ").strip()

    try:
        idade = int(input("Digite sua idade: ").strip())
    except ValueError:
        print("idade inválida\n")
        return
    if idade < 18:
        print(f"\n❌ {nome} você não pode se cadastrar nessa loja porque tem idade baixa ❌\n")
        return

    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    email = input("Coloque seu E-mail: ").strip()

    while True:
        senha = input("🔒 Digite sua senha: ")
        confirma_senha = input("🔒 Confirme sua senha: ")
        if senha == confirma_senha:
            print(f"\n✅ Senha cadastrada com sucesso {nome}! ✅")
            break
        else:
            print(f"\n❌ As senhas não são as mesmas {nome} ❌")

    while True:
        cpf = input("Digite seu CPF (11 dígitos): ").strip()
        if len(cpf) == 11 and cpf.isdigit():
            print("CPF válido")
            break
        else:
            print("❌ CPF inválido. Não exatamente 11 dígitos ❌")
    
    dados = {
        "nome": nome,
        "idade": idade,
        "data de nascimento": data_de_nascimento,
        "email": email,
        "senha": senha,
        "cpf": cpf
    }
    if os.path.exists("loja.json"):
        with open("loja.json", "r", encoding="utf-8") as arquivo:
            try:
                banco = json.load(arquivo)
            except json.JSONDecodeError:
                banco = []
    else:
        banco = []
    
    banco.append(dados)
    with open("loja.json", "w", encoding="utf-8") as arquivo:
        json.dump(banco, arquivo, ensure_ascii=False, indent=4)
    
    print("\n✅ Cadastro salvo com sucesso em 'loja.json'!\n")

def opcao_escola():
    print("===-- Escola (Cadastro Completo) --===")
    nome = input("Nome completo: ").strip()

    try:
        idade = int(input("Idade: ").strip())
    except ValueError:
        print("idade inválida\n")
        return
    
    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    cpf = input("CPF (11 dígitos): ").strip()
    if not (len(cpf) == 11 and cpf.isdigit()):
        print("CPF inválido\n")
        return
    
    email = input("E-mail: ").strip()
    telefone = input("Telefone/WhatsApp: ").strip()
    endereco = input("Endereço (rua, número, cidade, estado): ").strip()
    curso = input("Curso/turma (ex: Ensino Médio / 3º ano / Curso X): ").strip()
    matricula = input("Número de matrícula (se tiver, senão deixe vazio): ").strip()

    while True:
        senha = input("🔒 Digite uma senha para o aluno: ")
        confirma = input("🔒 Confirme a senha: ")
        if senha == confirma:
            break
        print("As senhas não coincidem. Tente novamente")

    registro = {
        "nome": nome,
        "idade": idade,
        "data de nascimento": data_de_nascimento,
        "cpf": cpf,
        "email": email,
        "telefone": telefone,
        "endereco": endereco,
        "curso": curso,
        "matricula": matricula,
        "senha": senha
    }
    caminho = "escolas.json"
    lista = carregar_json(caminho)
    lista.append(registro)
    salvar_json(caminho, lista)
    print("\nCadastro escolar realizado com sucesso e salvo em 'escolas.json'")
    print("=======================")
    print("===-- Dados Salvos --===")
    for k, v in registro.items():
        if k != "senha":
            print(f"{k.capitalize().replace('_',' ')}: {v}")
        else:
            print("Senha: (oculta)")
    print("=======================\n")

def opcao_calculadora():
    print("===-- Calculadora --===")

    try:
        num1 = float(input("Primeiro número: ").strip())
        operador = input("Escolha um operador (+, -, *, /): ").strip()
        num2 = float(input("Segundo número: ").strip())
    except ValueError:
        print("Erro: inválido e use números\n")
        return
    
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("a divisão não pode ser por Zero\n")
            return
        resultado = num1 / num2
    else:
        print("Operador inválido\n")
        return
    print(f"O resultado é: {resultado}\n")

def opcao_real_para_dolar():
    print("===-- Real para Dolar --===")

    try:
        real = float(input("Quantos reais você tem (R$)? ").strip())
        cotacao = float(input("Digite a cotação (R$ por US$1): ").strip())
    except ValueError:
        print("ERRO: insira apenas números\n")
        return
    if cotacao == 0:
        print("Cotação inválida (não pode ser zero)\n")
        return
    dolar = real / cotacao
    print(f"R$ {real:.2f} equivale a US$ {dolar:.2f}\n")

def opcao_jogo_adivinhacao():
    print("===-- Jogo de Adivinhação --===")
    numero_secreto = random.randint(1, 100)
    tentativa = None

    print("Tente adivinhar o número entre 1 e 100")
    while tentativa != numero_secreto:
        try:
            tentativa = int(input("Qual seu palpite? ").strip())
        except ValueError:
            print("Palpite inválido, digite um número inteiro")
            continue
        if tentativa < numero_secreto:
            print("Muito baixo")
        elif tentativa > numero_secreto:
            print("Muito alto")
        else:
            print("Você acertou\n")

def opcao_sair():
    print("===-- Sair --===")
    while True:
        sair = input("Realmente quer sair? digite 'sim' para voltar ao menu ou 'não' para encerrar: ").strip().lower()
        if sair in ("sim", "s"):
            print("Voltando ao menu...\n")
            return False
        if sair in ("não", "nao", "n"):
            print("✅ Programa finalizado")
            return True
        print("Resposta inválida. É 'sim' ou 'não'")

def trata_alias(opcao):
    o = opcao.strip().lower()
    if o in ("1", "loja", "shop"):
        return "loja"
    if o in ("2", "escola", "school", "cadastro escola"):
        return "escola"
    if o in ("3", "calculadora", "calc", "calculador"):
        return "calculadora"
    if o in ("4", "real para dolar", "realparadolar", "real para dólar", "dolar", "dólar"):
        return "realpara"
    if o in ("5", "jogo", "adivinhacao", "adivinhação", "jogo de adivinhação"):
        return "jogo"
    if o in ("6", "sair", "exit", "quit"):
        return "sair"
    return ""

def main():
    while True:
        opcao = exibir_menu()
        chave = trata_alias(opcao)
        if chave == "loja":
            opcao_loja()
        elif chave == "escola":
            opcao_escola()
        elif chave == "calculadora":
            opcao_calculadora()
        elif chave == "realpara":
            opcao_real_para_dolar()
        elif chave == "jogo":
            opcao_jogo_adivinhacao()
        elif chave == "sair":
            if opcao_sair():
                sys.exit(0)
        else:
            print("Opção inválida. Digite uma opção válida.\n")

if __name__ == "__main__":
    main()