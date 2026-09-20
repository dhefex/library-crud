from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)
 

    def show_infos(self):
            print("\nCadastro do usuário")
            print(f"Nome do usuário: {self.nome}")
            print(f"E-mail: {self.email}")
            print(f"Telefone: {self.telefone}")



#nome = input("Digite o nome do usuário: ")
#email = input("Digite o e-mail do usuário: ")
#telefone = input("Digite o telefone")

#register = User_register(nome, email, telefone)a

#register.show_infos()

        
        