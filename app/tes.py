from funcao import calcular_idade
import json

arquivo = open("arquivo.json", "r")
lista = list(json.load(arquivo))

for dicionario in lista:
    nome = dicionario["nome"]
    idade = dicionario["nascimento"]

    idade = calcular_idade(idade)
    
    if idade == -1:
        print('invalida')
        continue

    print("\n\n")
    print(f"seu nome é {nome}, sua idade é {idade}")


perguta = input("deseja adicionar algum nome e nascimento? (s/n) ")

if perguta.upper() == "S":
    nome = input("qual o nome que deseja adicionar? ")
    nascimento = input("qual o nascimento? ")

    pessoa_nova = {
        "nome": nome,
        "nascimento":nascimento
    }

    lista.append(pessoa_nova)


print('fim!')


with open('arquivo.json', 'w+') as f:
    f.write(json.dumps(lista, indent=4))
