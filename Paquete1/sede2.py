from Paquete1.Almacen import Almacen_base
class Almacen2(Almacen_base):
    def __init__(self, nombre, direccion, telefono):
        super().__init__(nombre, direccion, telefono)
        # Configurar el rango de impuestos para la sede sur
        self.rango_impuesto = (6, 8)
        # Configurar los productos específicos para esta sede
        self.productos['p1']['cantidad'] = int(2000 * 0.45)  # 0.55 es el 55% de cantidad zapatos
        self.productos['p2']['cantidad'] = int(3000 * 0.45)