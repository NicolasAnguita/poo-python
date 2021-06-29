#Crea una clase de Python llamada MathDojo que tenga un atributo, resultado y 2 métodos: sumar y restar. 
#Los 2 métodos deben tomar al menos 1 parámetro, pero podrían tomar muchos más.

# Crear una clase de MathDojo

class MathDojo:
    def __init__(self):
        self.result = 0

#Escriba el método add y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez

    def add(self, num, *nums):
        for n in nums:
            num += n
        self.result += num
        return self

#Escriba el método de subtract y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez

    def subtract(self, num, *nums):
        for n in nums:
            num += n
        self.result -= num
        return self


# crear una instruccion:
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)


# para probar:


# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)	
# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!