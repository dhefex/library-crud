from base import Base
from datetime import datetime 
from database import engine, SessionLocal
from models.book import Book
from models.loan import Loan
from models.users import User
from crud.remove import remove_book
from crud.update import update_book
from crud.update import update_loan
from crud.update import update_user
from crud.read import read_book
from crud.read import read_loan
from crud.read import read_users
from crud.remove import remove_book
from crud.remove import remove_loan
from crud.remove import remove_users
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(engine)

def register_book():
    while True:
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        isbn = input("Digite o ISBN")
        ano = int(input("Digite o ano: "))

        book = Book(
            titulo =titulo,
            autor=autor,
            isbn=isbn,
            ano = ano 

        )

        session = SessionLocal()
        session.add(book)
       # session.commit()

       # session.close()

        try:
            session.commit()
            print("Livro cadastrado com sucesso")

        except IntegrityError:
            session.rollback()
            print("Erro: Este ISBN já está cadastrado.")

        while True:
            choose = input("Deseja continuar ou sair? s/n):")
            if choose in ['yes','y']:
                print("Rodando aplicação!")
                break

            elif choose in ['not','n']:
                print("Bye Bye")
                return

            else:
                print("Erro, Opção inválida")
                


def register_loan():
    while True:
        id = input("Digite o ID do usuário")
        user = input("Nome do usuário: ")
        email = input("Digite o email do usuário: ")
        livro = input("Livro que será emprestado: ")
        devolucao = input("Data de devolução (DDMMYYYY):")
        devolucao = datetime.strptime(devolucao, "%d%m%Y").date()

        loan = Loan(
            id = id,
            user = user,
            email = email,
            livro = livro,
            devolucao = devolucao
        )

        session = SessionLocal()
        session.add(loan)
        session.commit()

        print("Livro cadastrado com sucesso!")

 

        while True:
            choose = input("Deseja continuar ou sair? s/n):")
            if choose in ['yes','y']:
                print("Rodando aplicação!")
                break

            elif choose in ['not','n']:
                print("Bye Bye")
                return

            else:
                print("Erro, Opção inválida")
                

def register_user():
    while True:
        id = input("Digite o ID do usuário: ")
        user = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")

        user = User(
            id = id,
            user = user,
            email = email
        )

        session = SessionLocal()
        session.add(user)
        session.commit()

        print("User cadastrado com sucesso!")


 

        while True:
            choose = input("Deseja continuar ou sair? s/n):")
            if choose in ['yes','y']:
                print("Rodando aplicação!")
                break

            elif choose in ['not','n']:
                print("Bye Bye")
                return

            else:
                print("Erro, Opção inválida")
                



def menu():
    while True:
        print("\nMENU")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Cadastrar usuário")
        print("4 - Listar informações")
        print("5 - Atualizar informações")
        print("6 - Excluir informações")


        choose = input("Escolha uma das opções: ")

        if not choose:
            print("Erro, Tente novamente")
            continue

        if choose == "1":
            register_book()

        elif choose == "2":
            register_loan()

        elif choose == "3":
            register_user()

        elif choose == "4":
            while True:
                print("1 - Livros cadastrados")
                print("2 - Livros emprestados")
                print("3 - Usuários cadastrados")
                option = input("Qual informação você deseja ver?:")

                if not option:
                    print("Esse campo não pode ficar vazio")
                    continue

                elif option == "1":
                    read_book()

                elif option == "2":
                    read_loan()

                elif option == "3":
                    read_users()



        elif choose == "5":
            while True:
                print("1 - Atualizar livros")
                print("2 - Atualizar empréstimos")
                print("3 - Atualizar Usuários")

                option = input("Qual opção informação você deseja atualizar?")

                if not option:
                    print("Esse campo não pode ficar vazio")
                    continue

                elif option == "1":
                    id_livro = int(input("Digite o ID do livro:"))
                    update_book(id_livro)

                elif option == "2":
                    id_emprestimos = int(input("Digite o ID do empréstimo: "))
                    update_loan(id_emprestimos)

                elif option == "3":
                    id_user = int(input("Digite o ID do usuário: "))
                    update_user(id_user)

                else:
                    print("Opção inválida tente novamente!")
          


           


        elif choose == "6":
            while True:
                print("1  - Excluir livros")
                print("2  - Excluir empréstimos")
                print("3  - Excluir Usuários")

                op = input("Quais das opções deseja excluir?:")

                if op == "1":
                    remove_book()

                elif op == "2":
                    remove_loan()

                elif op == "3":
                    remove_users()

                else:
                    print("Opção inválida, tente novamente")



        else:
            print("Erro, tente novamente!")



menu()




    


