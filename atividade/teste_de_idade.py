from funcao import calcular_idade
import json

arquivo = open("arquivo.json", "r")
lista = json.load(arquivo)

for dicionario in lista:
    nome = dicionario["nome"]
    idade = dicionario["nascimento"]

    idade = calcular_idade(idade)
    
    if idade == -1:
        print('invalida')
        continue

    print("-"*30)
    print(f"seu nome é {nome}, sua idade é {idade}")
    print("-"*30)


print('fim!')
