from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


from base import Base 


class Loan(Base):
    __tablename__ = "loan"
    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)
    livro: Mapped[str] = mapped_column(String(200), nullable=False)
    devolucao: Mapped[date] = mapped_column(nullable=False)
  

   # def show_info(self):
            #print(f"Livro emprestado: {self.book}")
            #print(f"Usuário: {self.user}")
            #print(f"Data de devolução: {self.loan_date}")



#livro = input("Livro emprestado: ")
#user = input("Usuário: ")
#loan_date = input("Data de devolução: ")

#register = loan(livro,user,loan_date)

#register.show_info()


        