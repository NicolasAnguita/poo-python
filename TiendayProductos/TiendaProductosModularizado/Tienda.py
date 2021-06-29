#from TiendaProductosModularizado.Productos import Productos

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