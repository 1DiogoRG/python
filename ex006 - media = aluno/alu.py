media_aluno = 0
aluno = 0
while True:
    try:
        nota = float(input("digite a sua primeira nota (digite 'sair' para finalizar): "))
        if nota == 'sair':
            break
        media_aluno += nota
        aluno += 1
    except ValueError:
        print("Por favor, insira um número válido para a nota")
        if aluno > 0:
            media = media_aluno / aluno
            print(f"a media da turme é {media}: ")
        else:
            print("Nenhuma nota foi inserida para calcular a média.")