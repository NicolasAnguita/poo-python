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

# haz que este método disminuya el saldo del usuario en la cantidad
    def make_withdrawal (self, amount): 
        self.account_balance -= amount
#haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
    def display_user_balance (self):
        print(f"Usuario : {self.name}, Saldo: $ {self.account_balance} ")

#haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
    def transfer_money (self, other_user, amount) :
        self.account_balance -= amount
        other_user.account_balance += amount

Nico = User("Nicolas", "jaja@jojo.cl")
Victor = User("Victor", "jeje@jojo.cl" )
Jimy = User("Jimy", "jiji@jojo.cl")


Nico.make_deposit(100)
Nico.make_deposit(400)
Nico.make_deposit(500)
Nico.display_user_balance()
Victor.make_deposit(800)
Victor.make_deposit(200)
Victor.make_withdrawal(250)
Victor.make_withdrawal(250)
Victor.display_user_balance()
Jimy.make_deposit(1000)
Jimy.make_withdrawal(200)
Jimy.make_withdrawal(200)
Jimy.make_withdrawal(200)
Jimy.display_user_balance()
Nico.transfer_money(Jimy, 200)
Nico.display_user_balance()
Jimy.display_user_balance()



