from tabulate import tabulate
from colorama import *
from utils.validaciones import validator
from models.data import productos,generarID,fechas,guardarDatos

init(autoreset=True)

def agregarProducto():
    print("---"*15)
    print("**MODULO AGREGAR PRODUCTOS**")
    id=generarID()
    nombreProducto=input("Ingrese Nombre Del Producto-->")
    marcaProducto=input("Ingrese Marca Del Porducto--->")
    categoriaProducto=input("Ingrese Categoria Del Producto-->")
    precioProducto=validator("Ingrese Precio Del Producto-->")
    stockProducto=validator("Ingrese Cantidad-->")
    garantiaProducto=validator("Ingrese Garantia En Meses-->")

    productos.append({
        "id":id,
        "Nombre":nombreProducto,
        "Marca":marcaProducto,
        "Categoria":categoriaProducto,
        "Precio":precioProducto,
        "Stock":stockProducto,
        "Garantia":garantiaProducto,
        "Fecha Registro":fechas()
    })

    guardarDatos()
    print("---"*15)
    print(f"Productos Guardados con Exito con id ->{id}")
    print("---"*15)


def listarInvetario():
    print("---"*15)
    print("**MODULO CONSULTAR INVENTARIO**")

    if not productos:
        print("No Hay Productos En El Inventario")
        return
    tabla=[]
    for info in productos:
        stockBajo=info["Stock"]

        colorStock=(f"{Fore.RED}{stockBajo}{Style.RESET_ALL}"   
                    if stockBajo <5
                    else 
                    str(stockBajo)
                    )
        
        aviso=(
            f"{Fore.RED} POCAS UNIDADES {Style.RESET_ALL}"
            if stockBajo <5
            else
            ""
        )
        tabla.append([
            info["id"],
            info["Nombre"],
            info["Marca"],
            info["Categoria"],
            info["Precio"],
            colorStock,
            aviso
        ])

    print(tabulate(tabla,headers=["ID","NOMBRE","MARCA","CATEGORIA","PRECIO","STOCK","ANUNCIO"],tablefmt="grid"))



def actualizarProducto():
    print("**MODULO ACTUALIZAR PRODUCTO**") 

    if not productos:
        print("No hay Productos en el inventario")
        return
    
    productoActualizar=validator("Ingrese ID Del Producto-->")

    for info in productos:
        if info.get("id")==productoActualizar:
            info["Precio"]=validator("Ingrese Nuevo precio-->")
            info["Stock"]=validator("Ingrese Nuevo Stock-->")
            info["Fecha Registro"]=fechas()
            guardarDatos()
            print("---"*15)
            print("Datos Actualizados**")
            return
    print("---"*15)
    print("No se encontro Producto con ese  ID")
    print("---"*15)

def eliminarProducto():
    print("**MODULO ELIMINAR PRODUCTOS**")
    
    productoEliminar=validator("Ingrese ID de Producto a Eliminar-->")

    for info in productos:
        if info.get("id")==productoEliminar:
            productos.remove(info)
            guardarDatos()
            print("Producto Eliminado Satisfactoriamente")
            return
    print("---"*15)
    print("Producto No encontrado")
