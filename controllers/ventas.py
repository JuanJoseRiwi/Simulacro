import tabulate
from utils.validaciones import validator
import models.data as db
from models.data import fechas

def registrarVentas():
    print("Tipo de Cliente\n1. Cliente Natural\n2. Cliente Mayorista")
    tipoCliente = input("Ingrese el tipo del cliente -> ")

    match tipoCliente:

        case "1":
            cliente = "Natural"
            productoVendido = input("Ingrese el producto -> ")

            for p in db.productos:
                if p.get("Nombre") == productoVendido:
                    print("Si está el producto")
                    print(f"Cantidad disponible: {p['Stock']}")

                    cantidad = validator("Ingrese la cantidad -> ")

                    if cantidad > p["Stock"]:
                        print("No hay esa cantidad")
                        return

                    nombreCliente = input("Ingrese el nombre del cliente -> ")
                    total = p["Precio"] * cantidad
                    p["Stock"] -= cantidad

                    db.ventas.append({
                        "Tipo Cliente": cliente,
                        "cliente": nombreCliente,
                        "producto": productoVendido,
                        "marca": p["Marca"],
                        "categoria": p["Categoria"],
                        "precio": p["Precio"],
                        "cantidad": cantidad,
                        "total": total,
                        "fecha": fechas()
                    })

                    db.guardarDatos()
                    return

            print("Producto no encontrado")

        case "2":
            cliente = "Mayorista"
            productoVendido = input("Ingrese el producto -> ")

            for p in db.productos:
                if p.get("Nombre") == productoVendido:
                    print("Si está el producto")
                    print(f"Cantidad disponible: {p['Stock']}")
                    break
            else:
                print("Producto no encontrado")
                return

            cantidad = validator("Ingrese la cantidad -> ")

            if cantidad < 5:
                print("Venta mayorista: debe comprar mínimo 5 unidades.")
                return

            if cantidad > p["Stock"]:
                print("No hay esa cantidad disponible.")
                return

            nombreCliente = input("Ingrese el nombre del cliente -> ")

            precioUnitario = p["Precio"]
            totalSinDescuento = precioUnitario * cantidad
            descuento = totalSinDescuento * 0.10
            totalFinal = totalSinDescuento - descuento

            p["Stock"] -= cantidad

            print(
                f"Precio Unitario --> {precioUnitario} | "
                f"Total Sin Descuento --> {totalSinDescuento} | "
                f"Mayorista 10% Descuento | "
                f"Total Con Descuento --> {totalFinal}"
            )

            db.ventas.append({
                "Tipo Cliente": cliente,
                "cliente": nombreCliente,
                "producto": productoVendido,
                "marca": p["Marca"],
                "categoria": p["Categoria"],
                "precio": p["Precio"],
                "cantidad": cantidad,
                "descuento": descuento,
                "total": totalFinal,
                "fecha": fechas()
            })

            db.guardarDatos()

        case _:
            print("Opción inválida")


def verVentas():
    if not db.ventas:
        print("No hay ventas registradas.")
        return

    tabla = []

    for v in db.ventas:
        tipoCliente=v.get("Tipo de Cliente") or v.get("Tipo Cliente") or ""
        totalFormateado=f"{v.get("total",0):,.0f}".replace(",",".")
        tabla.append([
            tipoCliente,
            v.get("cliente", ""),
            v.get("producto", ""),
            v.get("cantidad", ""),
            totalFormateado
            
        ])

    print(tabulate.tabulate(
        tabla,
        headers=["Tipo de cliente","Cliente", "Producto", "Cantidad", "Total"],
        tablefmt="grid"
    ))