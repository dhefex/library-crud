from models.book import Book
from models.loan import Loan
from models.users import User
from database import SessionLocal
from database import sessionmaker
from sqlalchemy import select

session = SessionLocal()

# Remove os livros
def remove_book():
    while True:
        id_book = int(input("Digite o ID do livro que deseja excluir: "))

        # Verificando se o ID existe
        livro = session.scalars(
            select(Book).where(Book.id == id_book)
        ).first()

        if livro:
            session.delete(livro)
            session.commit()
            print("Livro excluído com sucesso!")

        else:
            print("Livro não foi encontrado!")
            

        # Gerenciamento
        while True:
            choose = input("Deseja sair continuar ou sair? (Y/N): ")
        

            if choose in ["n","no","N"]:
                print("Aplicação rodando")
                break

            elif choose in ["yes","y","Y"]:
                print("Bye Bye...")
                return
                

            else:
                print("Erro, opção inválida!")
# Remove emprestímos
def remove_loan():
    while True:
        id_loan = int(input("Digite o ID do empréstimo:"))

        loans = session.scalars(
            select(Loan).where(Loan.id == id_loan)
        ).first()

        if loans:
            session.delete(loans)
            session.commit()
            print("Empréstimo excluído")

        else:
            print("Emprestímo não encontrado")

            # Gerenciamento
        while True:
            choose = input("Deseja sair continuar ou sair?")
            print("Y or N")
        
            if choose in ["yes","y","Y"]:
                print("Bye Bye...")
                break

            elif choose in ["not","n","N"]:
                print("Aplicação rodando")
                return

            else:
                print("Erro, opção inválida!")


def remove_users():
    while True:
        id_user = int(input("Digite o ID do usuário: "))

        users = session.scalars(
            select(User).where(User.id == id_user)
        ).first()

        if users:
            session.delete(users)
            session.commit()
            print("Usuário removido com sucesso!")

        else:
            print("Usuário não encontrado!")


    # Gerenciamento
        while True:
            choose = input("Deseja sair continuar ou sair?")
            print("Y or N")

            if choose in ["yes","y","Y"]:
                print("Bye Bye...")
                break

            elif choose in ["no","n","N"]:
                print("Aplicação rodando")
                return

            else:
                print("Erro, opção inválida!")




