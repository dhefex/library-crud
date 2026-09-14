
class Loan:
    def __init__(self, book, user, loan_date ):
        self.book = book
        self.user = user
        self.loan_date = loan_date

    def show_info(self):
            print(f"Livro emprestado: {self.book}")
            print(f"Usuário: {self.user}")
            print(f"Data de devolução: {self.loan_date}")



#livro = input("Livro emprestado: ")
#user = input("Usuário: ")
#loan_date = input("Data de devolução: ")

#register = loan(livro,user,loan_date)

#register.show_info()


        