
class User_register:
    def __init__(self,nome,email,telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def show_infos(self):
            print("\nCadastro do usuário")
            print(f"Nome do usuário: {self.nome}")
            print(f"E-mail: {self.email}")
            print(f"Telefone: {self.telefone}")



#nome = input("Digite o nome do usuário: ")
#email = input("Digite o e-mail do usuário: ")
#telefone = input("Digite o telefone")

#register = User_register(nome, email, telefone)

#register.show_infos()

        
        