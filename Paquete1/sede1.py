from Paquete1.Almacen import Almacen_base

class Almacen1(Almacen_base):
    def __init__(self, nombre, direccion, telefono):
        super().__init__(nombre, direccion, telefono)
        # Configurar el rango de impuestos para la sede norte
        self.rango_impuesto = (10, 12)
        # Configurar los productos específicos para esta sede
        self.productos['p1']['cantidad'] = int(2000 * 0.55)  # 55% del inventario total
        self.productos['p2']['cantidad'] = int(3000 * 0.55)