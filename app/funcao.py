from datetime import date

hoje = date.today()

def calcular_idade(data_de_nascimento: str):

    if len(data_de_nascimento) != 10:
        print("erro")
        return -1
        
    for caracter in data_de_nascimento:
        if caracter not in "/0123456789":
            return -1
    
    data_de_nascimento = data_de_nascimento.split('/') 
    
    nascimento = {
        "ano":int(data_de_nascimento[2]),
        "dia":int(data_de_nascimento[0]),
        "mes":int(data_de_nascimento[1])
    }
    
    match nascimento["mes"]:
        case  1|3|5|7|8|10|12:  # meses de 31 dias
            if nascimento["dia"] < 1 or nascimento["dia"] >31:
                print("erro na dia,digite a data novamente")
                return -1
        case 4|6|9|11:  # meses de 30 dias 
            if nascimento["dia"] < 1 or nascimento["dia"] > 30:
                print("erro na dia,digite a data novamente")   
                return -1
        case _:  # meses de 29 dias(se o dia for menor ou maior que 29 ou seja se for 30 acima)
            if nascimento["dia"] < 1 or nascimento["dia"] > 29:
                print("erro na dia,digite a data novamente")
                return -1                    
    
    idade = int(hoje.year - nascimento["ano"])
    
    if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
        idade -= 1  # idade = idade - 1
    
    return idade
