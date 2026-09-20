from models.book import Book
from models.loan import Loan
from models.users import User
from database import SessionLocal
from database import sessionmaker
from datetime import datetime


def update_book(id):

    session = SessionLocal()
    livro = session.get(Book, id)

    if livro:
        print(f"\nLivro atual: {livro.title}")


        novo_titulo = input("Novo título: ")
        novo_autor = input("Novo autor:")
        novo_isbn = input("Novo ISBN: ")
        novo_ano = input("Novo ano: ")

        livro.title = novo_titulo
        novo_autor = novo_autor
        novo_isbn = novo_isbn
        novo_ano = novo_ano

        session.commit()

        print("Livro atualizado com sucesso!")

    else:
        print("Livro não foi encontrado")



def update_loan(id):
    session = SessionLocal()

    loan = session.get(Loan, id)

    if loan:
        print("\nInformações atuais: ")
        print(f"ID: {loan.id}")
        print(f"Livro: {loan.livro}")
        print(f"Usuário: {loan.user}")
        print(f"E-mail: {loan.email}")
        print(f"Devolução: {loan.devolucao}")

        novo_id= int(input("Digite o novo ID do usuário: "))
        novo_user = input("Digite o novo  usuário: ")
        novo_email = input("Digite o novo email do usuário:")
        loan_livro = input("Livro que será emprestado")
        devolucao = input("Data de devolucao")
        devolucao = datetime.strptime(devolucao,"%d%m%Y")

        loan.id= int(novo_id)
        loan.user = novo_user
        loan.email = novo_email
        loan.devolucao = devolucao

        session.commit()

        print("Empréstimo atualizado")

    else:
        print("Empréstimo não encontrado!")

def update_user(id):
    session = SessionLocal()

    users = session.get(User, id)

    if users:
        print("\nInformações atuais")
        print(f"ID: {User.id}")
        print(f"Usuário: {User.user}")
        print(f"E-mail: {User.email}")

        novo_id = int(input("Digite o novo id do usuário: "))
        novo_user = input("Digite um novo usuário: ")
        novo_email = input("Digite um novo email: ")

        users.user = novo_user
        users.id = int(novo_id)
        users.email = novo_email

        session.commit()

        print("Usuário não encontrado atualizado!")

    else:
        print("Usuário não encontrado!")


def menu():
    while True:
        print("\nMENU")
        print("1 - Atualizar Livro")
        print("2 - Atualizar empréstimo")
        print("3 - Atualizar usuário")

        choose = input("Escolha uma das opções: ")

        if not choose:
            print("Esse campo não pode ficar vazio!")
            continue

        elif choose == "1":
            update_book(id)

        elif choose == "2":
            update_loan(id)

        elif choose == "3":
            update_user(id)

        else:
            print("Valor inválido, tente novamente!")

# menu()
        




    
