#crea una clase  tienda con 2 atributos
class Tienda():
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
# toma un producto y lo agrega a la tienda
    def add_product (self, new_product):
        self.productos.append(new_product)
        print(f"Se agrego el producto {new_product.nombre}")
        return self
# elimina el producto de la lista de productos de la tienda dada la identificación 
# (suponga que id es el índice del producto en la lista) e imprima su información.
    def sell_product (self, id):
        eliminado = self.productos.pop(id)
        print(f"Se ha vendido {eliminado.nombre} ")
        return self

#aumenta el precio de cada producto por el percent_increase dado
# (¡use el método que escribió en la clase Product!)
    def inflation(self, percent_increase):
        for producto in self.productos:
            producto.update_price(percent_increase, True)
        return self

#actualiza todos los productos que coinciden con la categoría dada reduciendo el precio en el percent_discount dado
#(¡use el método que escribió en la clase Product!)
    def set_clearance (self, category, percent_discount):
        for producto in self.productos:
            if producto.categoria== category:
                producto.update_price(percent_discount, False)
        return self
        

#crea una clase  producto con 3 atributos

class Productos():
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

#actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado.
# Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.precio = self.precio*(1 + percent_change)
        else:
            self.precio -= self.precio * percent_change
            
#Agrega el método print_info a la clase de Producto
#imprime el nombre del producto, su categoría y su precio.
    def print_info (self):
        print(f"El producto se llama {self.nombre}, su categoria es {self.categoria}, y su precio es ${self.precio}")


#Prueba tus clases creando una instancia de la Tienda y algunas instancias de la clase Producto,

ciclotienda = Tienda("Ciclotienda")
trek = Productos("Trek2021", 300000, "montaña")
ciclesvilla = Productos("ciclesvilla190", 190000, "urbana")
triciclo = Productos("triciclo", 70000, "niños")

# agrega esas instancias a la instancia de la tienda y luego prueba los métodos.
ciclotienda.add_product(trek).add_product(ciclesvilla).add_product(triciclo)
ciclotienda.sell_product(0)
ciclotienda.inflation(0.10)
ciclotienda.set_clearance("niños", 0.20)

for producto in ciclotienda.productos:
    producto.print_info()



