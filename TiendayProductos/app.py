from TiendaProductosModularizado.Productos import Productos
from TiendaProductosModularizado.Tienda import Tienda

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