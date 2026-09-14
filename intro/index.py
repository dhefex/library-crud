class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos"



pessoa1 = Pessoa("Ana", 25)
print(pessoa1.nome)
print(pessoa1.apresentar())


        
