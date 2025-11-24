from controllers.inventario import agregarProducto,listarInvetario,actualizarProducto,eliminarProducto
from controllers.ventas import registrarVentas,verVentas
from controllers.reportes import reporteVentasPorMarca,reporteTop3,reporteIngresos

#menu principal el cual sera llamado desde el main (orquestador), pagina de menu de opciones
def menu():
    #constante para el while
    constante=True

    while constante:
     print("""
           Bienvenidos A ELectronicos S.A
           1. Agregar Producto
           2. Listar Inventario
           3. Actualizar Producto
           4. Eliminar Producto
           5. Registrar Venta
           6. Ver Ventas
           7. Reporte Ventas Por Marca
           8. Reporte Top 3 Productos Vendidos
           9. Reporte Ingresos Totales
            0. Salir""")
        
 
     opcion=input("Ingrese Opcion-->")
     #selector de opciones
     match opcion:
        case "1":
           agregarProducto()
        case "2":
           listarInvetario()
        case "3":
           actualizarProducto()
        case "4":
           eliminarProducto()
        case "5":
           registrarVentas()
        case "6":
           verVentas()
        case "7":
           reporteVentasPorMarca()
        case "8":
           reporteTop3()
        case "9":
           reporteIngresos()
        case "0":
           constante=False
        case _:
           print("Invalid Option")