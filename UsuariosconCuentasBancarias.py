
#No deberías tener que cambiar nada en la clase BankAccount. 
class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.balance -=5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        return f"Saldo : $ {self.balance}"
        
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance * (self.int_rate+1)
            return self
        else:
            print("No tiene saldo")
            return self
#Actualiza tu clase de usuario existente para tener una asociación con la clase BankAccount. 
#Las firmas de método de la clase Usuario (la primera línea del método con la palabra clave def) también deben permanecer iguales.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount) 

    def make_withdraw(self, amount):
        self.account.withdraw(amount)

    def display_user_balance (self):
        print(f"Usuario : {self.name}, {self.account.display_account_info()} ")


Nico=User("Nico", "ja@jo.cl")

Nico.make_deposit(100)
Nico.make_withdraw(60)
Nico.display_user_balance()

