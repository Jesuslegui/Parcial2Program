## Jesus david leguizamo velasco 
## Jackeline Garcia Toro

class Almacen_base:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = {
            'p1':{
                'nombre': 'Tenis',
                'precio': 150000,
                'cantidad':2000
            },
            'p2':{
                'nombre': 'Botas ',
                'precio': 350000,
                'cantidad': 3000
            }
        }
        self.impuesto = 0
        self.total_ventas = 0

    
    def AsignarProducto(self, id_producto, nombre, precio, cantidad):
        if not isinstance(precio, int) or not isinstance(cantidad, int):
            raise TypeError("El precio y la cantidad deben ser valores enteros.")
        self.productos[id_producto] = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        
         
    def ConfigurarImpuestoLocal(self, impuesto):
        if not isinstance(impuesto, int):
            raise TypeError("El impuesto debe ser un valor entero.")
        if not (self.rango_impuesto[0] <= impuesto <= self.rango_impuesto[1]):
            raise ValueError(f"El impuesto debe estar entre {self.rango_impuesto[0]}% y {self.rango_impuesto[1]}%.")
        self.impuesto = impuesto


    def vender(self, id_producto, cantidad):
        if id_producto in self.productos:
            if cantidad <= self.productos[id_producto]['cantidad']:
                self.productos[id_producto]['cantidad'] -= cantidad
                total_venta = self.productos[id_producto]['precio'] * cantidad
                total_venta += total_venta * self.impuesto / 100
                self.total_ventas += total_venta
                return True, total_venta
            else:
                return False, f"No hay suficiente cantidad del producto {id_producto}."
        else:
                return False, f"Producto {id_producto} no encontrado."
    
    def revisar_inventario (self):
         return {id_producto: prod['cantidad'] for id_producto, prod in self.productos.items()}
    
print ("Fin del programa")
    


