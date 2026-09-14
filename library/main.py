from base import Base
from database import engine, SessionLocal
from models.book import Book

Base.metadata.create_all(engine)

def register_book():
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
    session.commit()

    session.close()

    print("Livro cadastrado com sucesso")

register_book()

