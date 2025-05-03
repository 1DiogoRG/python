def nome_idade():  
    nome = input("\ncomo se chama meu jovem: ")
    idade = int(input("quantos anos você tem?: "))   
    if idade < 15:
        print("adolescente")
        return  
    elif idade >= 16:
        print("HMMMMMMMMMMMMMM já é adulto")
        return   
    print("\nSeus dados")
    print(f"NOME: {nome}, IDADE: {idade}")
nome_idade()