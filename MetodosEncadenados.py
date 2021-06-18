class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def __str__(self):
        return self.name

#haz que el usuario haga un desposito
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

# haz que este método disminuya el saldo del usuario en la cantidad
    def make_withdrawal (self, amount): 
        self.account_balance -= amount
        return self
#haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
    def display_user_balance (self):
        print(f"Usuario : {self.name}, Saldo: $ {self.account_balance} ")

#haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
    def transfer_money (self, other_user, amount) :
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Nico = User("Nicolas", "jaja@jojo.cl")
Victor = User("Victor", "jeje@jojo.cl" )
Jimy = User("Jimy", "jiji@jojo.cl")


Nico.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()




