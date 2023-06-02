from pessoa import Pessoa
import json

arquivo = open("arquivo.json", "r")
lista = list(json.load(arquivo))

for pessoa in lista:
    pessoa_obj = Pessoa(
        pessoa["nome"],
        pessoa["nascimento"])

    
    if pessoa_obj.idade == -1:
        print('invalida')
        continue

    print("\n\n")
    print(f"seu nome é {pessoa_obj.nome}, sua idade é {pessoa_obj.idade}")


perguta = input("deseja adicionar algum nome e nascimento? (s/n) ")

if perguta.upper() == "S":
    nome = input("qual o nome que deseja adicionar? ")
    nascimento = input("qual o nascimento? ")

    pessoa_nova = Pessoa(nome, nascimento)

    lista.append(pessoa_nova.to_dict())


print('fim!')


with open('arquivo.json', 'w+') as f:
    f.write(json.dumps(lista, indent=4))
