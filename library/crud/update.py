from models.book import Book
from models.loan import Loan
from models.users import User
from database import SessionLocal
from database import sessionmaker
from datetime import datetime

# Atualizando informações
def update_book(id):
    session = SessionLocal()
    # Buscando o ID do livro
    livro = session.get(Book, id)

     # Verificando
    if livro:
        print(f"\nLivro atual: {livro.titulo}")

        novo_titulo = input("Novo título: ")
        novo_autor = input("Novo autor: ")
        novo_isbn = input("Novo ISBN: ")
        novo_ano = input("Novo ano: ")

        livro.titulo= novo_titulo
        livro.autor = novo_autor
        livro.isbn= novo_isbn
        livro.ano = novo_ano

        session.commit()

        print("Livro atualizado com sucesso!")

    else:
        print("Livro não foi encontrado")

    session.close()

def update_loan(id):
    session = SessionLocal()

    loan = session.get(Loan, id)

    if loan:
        print("\nInformações atuais:")
        print(f"ID: {loan.id}")
        print(f"Livro: {loan.livro}")
        print(f"Usuário: {loan.user}")
        print(f"E-mail: {loan.email}")
        print(f"Devolução: {loan.devolucao}")

        novo_user = input("Digite o novo usuário: ")
        novo_email = input("Digite o novo email do usuário: ")
        novo_livro = input("Livro que será emprestado: ")
        devolucao = input("Data de devolução (DDMMAAAA): ")

        devolucao = datetime.strptime(devolucao, "%d%m%Y")

        loan.user = novo_user
        loan.email = novo_email
        loan.livro = novo_livro
        loan.devolucao = devolucao

        session.commit()

        print("Empréstimo atualizado!")

    else:
        print("Empréstimo não encontrado!")

    session.close()

def update_user(id):
    session = SessionLocal()

    user = session.get(User, id)

    if user:
        print("\nInformações atuais")
        print(f"ID: {user.id}")
        print(f"Usuário: {user.user}")
        print(f"E-mail: {user.email}")

        novo_user = input("Digite um novo usuário: ")
        novo_email = input("Digite um novo email: ")

        user.user = novo_user
        user.email = novo_email

        session.commit()

        print("Usuário atualizado com sucesso!")

    else:
        print("Usuário não encontrado!")

    session.close()








    
