from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from base import Base



class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    autor: Mapped[str] = mapped_column(String(200), nullable=False)

    isbn: Mapped[str] =  mapped_column(
          String(200),
          unique=True,
          nullable=False,
    )

    ano: Mapped[int] = mapped_column(nullable=False)

  

    def show_info(self):
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"ISBN: {self.isbn}")
            print(f"Ano: {self.ano}")
          





# Criando o objeto e passando as informações dos atributos 

#titulo = input("Digite o título do livro: ")
#isbn = input("Digite o isbn do livro: ")
#ano = input("Digite o ano do livro: ")

#book = Book_register(titulo,autor,isbn,ano)

#book.show_info()

