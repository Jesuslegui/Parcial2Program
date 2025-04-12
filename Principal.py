from Paquete1.sede1 import Almacen1
from Paquete1.sede2 import Almacen2

def main():
    try:
        # Crear instancias de las sedes
        almacen1 = Almacen1("Almacén Norte", "Calle Norte", "123456789")
        almacen2 = Almacen2("Almacén Sur", "Calle Sur", "987654321")

        # Configurar impuestos
        try:
            almacen1.ConfigurarImpuestoLocal(11)  # Correcto
            almacen2.ConfigurarImpuestoLocal(7)   # Correcto
        except TypeError as e:
            print(f"Error al configurar impuesto: {e}")
        except ValueError as e:
            print(f"Error al configurar impuesto: {e}")

        # Asignar productos
        try:
            almacen1.AsignarProducto('p1', 'Tenis', 150000, 15)
            almacen2.AsignarProducto('p2', 'Botas', 350000, 35)
        except TypeError as e:
            print(f"Error al asignar producto: {e}")

        # Realizar ventas
        exito1, total1 = almacen1.vender('p1', 15)
        exito2, total2 = almacen2.vender('p2', 35)

        # Mostrar resultados de ventas
        print(f"Venta en Almacén Norte: {'Exitosa' if exito1 else 'Fallida'}, Total: {total1}")
        print(f"Venta en Almacén Sur: {'Exitosa' if exito2 else 'Fallida'}, Total: {total2}")

        # Revisar inventarios
        print("Inventario Almacén Norte:", almacen1.revisar_inventario())
        print("Inventario Almacén Sur:", almacen2.revisar_inventario())

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

if __name__ == "__main__":
    main()

print("Fin del programa")

