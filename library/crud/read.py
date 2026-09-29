from sqlalchemy import select
from database import SessionLocal
from models.book import Book
from models.loan import Loan
from models.users import User

# Liastando informações do livro
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


        if not books:
            print("Livro não encontrado")


def read_loan():
    with SessionLocal() as session:
        stmt = select(Loan)
        loans = session.scalars(stmt).all()

        for loan in loans:
            print(f"ID: {loan.id}")
            print(f"Livro emprestado: {loan.livro}")
            print(f"E-mail: {loan.email}")
            print(f"Usuário: {loan.user}")
            print(f"Devolução: {loan.devolucao}")


        if not loans:
            print("Empréstimo não encontrado")


def read_users():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()


        for user in users:
            print(f"ID: {user.id}")
            print(f"Usuário: {user.user}")
            print(f"E-mail: {user.email}")

        if not users:
            print("Usuário não encontrado")





    



