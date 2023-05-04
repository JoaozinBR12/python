from funcao import calcular_idade
import json

arquivo = open("arquivo.json", "r")
lista = list(json.load(arquivo))

lista.append({"nome":"teste","nascimento":"01/01/0000"})
lista.append({"nome":"carlin","nascimento":"20/05/1000"})

for dicionario in lista:
    nome = dicionario["nome"]
    idade = dicionario["nascimento"]

    idade = calcular_idade(idade)
    
    if idade == -1:
        print('invalida')
        continue

    print("\n\n")
    print(f"seu nome é {nome}, sua idade é {idade}")


print('fim!')


with open('arquivo.json', 'w+') as f:
    f.write(json.dumps(lista, indent=4))
