from datetime import date

hoje = date.today()
class Pessoa():
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.idade = self.calcular_idade()

    def to_dict(self):
        return {
            "nome": self.nome,
            "nascimento": self.nascimento
        }

    def calcular_idade(self):

        if len(self.nascimento) != 10:
            print("erro")
            raise TypeError
            
        for caracter in self.nascimento:
            if caracter not in "/0123456789":
                raise TypeError
        
        self.nascimento = self.nascimento.split('/') 
        
        nascimento = {
            "ano":int(self.nascimento[2]),
            "dia":int(self.nascimento[0]),
            "mes":int(self.nascimento[1])
        }
        
        match nascimento["mes"]:
            case  1|3|5|7|8|10|12:  # meses de 31 dias
                if nascimento["dia"] < 1 or nascimento["dia"] >31:
                    print("erro na dia,digite a data novamente")
                    raise TypeError
            case 4|6|9|11:  # meses de 30 dias 
                if nascimento["dia"] < 1 or nascimento["dia"] > 30:
                    print("erro na dia,digite a data novamente")   
                    raise TypeError
            case _:  # meses de 29 dias(se o dia for menor ou maior que 29 ou seja se for 30 acima)
                if nascimento["dia"] < 1 or nascimento["dia"] > 29:
                    print("erro na dia,digite a data novamente")
                    raise TypeError              
        
        idade = int(hoje.year - nascimento["ano"])
        
        if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
            idade -= 1  # idade = idade - 1
        
        return idade
