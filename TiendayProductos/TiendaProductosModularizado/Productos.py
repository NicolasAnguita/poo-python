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