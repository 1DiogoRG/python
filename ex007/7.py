#comando pra digitar a idade
idade = int(input("digite sua idade: "))

def pode_votar(idade):
    
    #se a idade for maior ou igual a 16, a pessoa pode votar
    if idade >= 16:
        #se idade for entre 18 e 70, o voto é obrigatório
        if idade >= 18 and idade <= 70:
            return "você pode votar, e o voto é obrigatório"
        else:
            return "você pode votar, mas é facultativo"
    
    else:
        #se idade for menor do que 16, a pessoa não pode votar
        return "você ainda não pode votar"
    
#exemplo de uso de algoritmo
resultado = pode_votar(idade)
print(resultado)