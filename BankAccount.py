# Primero, practiquemos más clases de escritura escribiendo una nueva clase de BankAccount . 
# En la próxima lección, vincularemos nuestras clases de usuario y cuenta bancaria.
#La clase BankAccount debe tener un saldo. 
# Cuando se crea una nueva instancia de BankAccount, si se proporciona un monto, el saldo de la cuenta debe establecerse inicialmente en ese monto; de lo contrario, el saldo debe comenzar en $ 0. 
# La cuenta también debe tener una tasa de interés, guardada como un decimal (es decir, el 1% se guardaría como 0.01), que debe proporcionarse cuando se instancia. (Sugerencia: cuando se usan valores predeterminados en los parámetros, ¡el orden de los parámetros es importante!)

#La clase también debe tener los siguientes métodos:

# deposit(self, cantidad) : aumenta el saldo de la cuenta en la cantidad dada
# withdraw(self, cantidad) : disminuye el saldo de la cuenta en la cantidad dada si hay fondos suficientes; si no hay suficiente dinero, imprima un mensaje "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
# display_account_info(self) - imprime en la consola: ej. "Saldo: $ 100"
# yield_interest(self) : aumenta el saldo de la cuenta en el saldo actual * la tasa de interés (siempre que el saldo sea positivo)

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
        print(f"Saldo : $ {self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance * (self.int_rate+1)
            return self
        else:
            print("No tiene saldo")
            return self

cuenta1 = BankAccount(0.01,0)
cuenta2 = BankAccount(0.03,100)
cuenta1.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
cuenta2.deposit(150).deposit(250).withdraw(50).withdraw(50).withdraw(100).withdraw(200).yield_interest().display_account_info()

