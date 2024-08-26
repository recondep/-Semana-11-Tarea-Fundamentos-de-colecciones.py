
# import json

class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def _init_(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad:
                self.productos[id].cantidad = cantidad
            if precio:
                self.productos[id].precio = precio
        else:
            print("Producto no encontrado en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as file:
            json.dump([producto._dict_ for producto in self.productos.values()], file)

    def cargar_inventario(self, archivo):
        with open(archivo, 'r') as file:
            data = json.load(file)
            for item in data:
                producto = Producto(item['id'], item['nombre'], item['cantidad'], item['precio'])
                self.productos[producto.id] = producto

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("\n1. Añadir producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

# Ejemplo de uso
inventario = Inventario()

# Cargar inventario desde archivo al iniciar el programa
inventario.cargar_inventario("inventario.json")

opcion = 0
while opcion != 6:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        id = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        inventario.añadir_producto(nuevo_producto)
        inventario.guardar_inventario("inventario.json")

    elif opcion == 2:
        id = int(input("Ingrese el ID del producto a eliminar: "))
        inventario.eliminar_producto(id)
        inventario.guardar_inventario("inventario.json")

    elif opcion == 3:
        id = int(input("Ingrese el ID del producto a actualizar: "))
        cantidad = int(input("Ingrese la nueva cantidad (deje en blanco si no desea modificar): "))
        precio = float(input("Ingrese el nuevo precio (deje en blanco si no desea modificar): "))
        inventario.actualizar_producto(id, cantidad, precio)
        inventario.guardar_inventario("inventario.json")

    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        inventario.buscar_producto_por_nombre(nombre)

    elif opcion == 5:
        inventario.mostrar_productos()

print("¡Gracias por usar el Sistema de Gestión de Inventario!")