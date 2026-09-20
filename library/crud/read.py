from sqlalchemy import select
from database import SessionLocal
from models.book import Book
from models.loan import Loan
from models.users import User


def read_book():
    with SessionLocal() as session:
        stmt = select(Book)
        books = session.scalars(stmt).all()

        for book in books:
            print(f"ID: {book.id}")
            print(f"Título: {book.titulo}")
            print(f"Autor: {book.autor}")
            print(f"ISBN: {book.isbn}")
            print(f"Ano: {book.ano}")
            print("-" * 30 )

    

def read_loan():
    with SessionLocal() as session:
        stmt = select(Loan)
        loans = session.scalars(stmt).all()


        for loan in loans:
            print(f"ID: {loan.id}")
            print(f"User: {loan.user}")
            print(f"E-mail: {loan.email}")
            print(f"Livro: {loan.livro}")
            print(f"Devolução: {loan.devolucao}")
            print("-" * 30)

def read_users():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()


        for user in users:
            print(f"ID: {user.id}")
            print(f"User: {user.user}")
            print(f"E-mail: {user.email}")


def menu():
    while True:
        print("\nVer informações")
        print("1 - Livros cadastrados")
        print("2 - Livros emprestados")
        print("3 - Usuários cadastrados")

        choose = input("Escolha uma das opções:")

        if not choose:
            print("É necessário escolher uma das opções!")
            continue

        elif choose == "1":
            read_book()

        elif choose == "2":
            read_loan()

        elif choose == "3":
            read_users()

        else:
            print("Opção inválida, tente novamente!")


# menu()
            



