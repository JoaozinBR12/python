from atividade.funcao import calcular_idade

nome = input("Digite seu nome: ")
while nome.lower() != "zero" and nome != "0":
    idade = calcular_idade()
    
    if idade == -1:
        print('invalida')
        continue

    print("-"*30)
    print(f"seu nome é {nome}, sua idade é {idade}")
    print("-"*30)

    nome = input("nome: ") 

print('fim!')
