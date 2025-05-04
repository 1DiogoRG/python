aluno = 1
while aluno <= 5:
    nota1 = float(input("\ndigite a primeira nota do aluno: "))
    nota2 = float(input("digite a segunda nota do aluno: "))
    nota3 = float(input("digite a terceira nota do aluno: "))
    nota4 = float(input("digite a quarta nota do aluno: "))
    media = (nota1 + nota2 + nota3 + nota4) / 3
    print(f"a media do aluno {aluno} é {media}")
    aluno = aluno + 1