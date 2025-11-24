
import json
import os
from datetime import datetime

archivo = "baseDeDatos.json"

def fechas():
    return datetime.now().strftime("%d/%m/%y")

productos = [
    {"id": 1, "Nombre": "Televisor", "Marca": "LG", "Categoria": "Electrodomestico", "Precio": 1500000, "Stock": 10, "Garantia": 12, "Fecha Registro": fechas()},
    {"id": 2, "Nombre": "Audifonos", "Marca": "SONY", "Categoria": "ACCESORIO", "Precio": 60000, "Stock": 20, "Garantia": 2, "Fecha Registro": fechas()},
    {"id": 3, "Nombre": "Parlante", "Marca": "JBL", "Categoria": "AUDIO", "Precio": 15000, "Stock": 15, "Garantia": 6, "Fecha Registro": fechas()},
    {"id": 4, "Nombre": "TECLADO", "Marca": "ASUS", "Categoria": "COMPUTACION", "Precio": 200000, "Stock": 18, "Garantia": 3, "Fecha Registro": fechas()},
    {"id": 5, "Nombre": "MOUSE", "Marca": "LOGITECH", "Categoria": "COMPUTACION", "Precio": 35000, "Stock": 30, "Garantia": 6, "Fecha Registro": fechas()}
]

ventas = []


# ----------------------------------------------------------
# GUARDAR DATOS
# ----------------------------------------------------------
def guardarDatos():
    data = {
        "productos": productos,
        "ventas": ventas
    }

    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Se guardó con éxito el cambio en el JSON")
    except:
        print("Error al guardar")


# ----------------------------------------------------------
# CARGAR DATOS 
# ----------------------------------------------------------
def cargarDatos():
    global productos, ventas

    if not os.path.exists(archivo):
        return

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            data = json.load(file)

            
            productos.clear()
            productos.extend(data.get("productos", []))

            ventas.clear()
            ventas.extend(data.get("ventas", []))

        print("Datos cargados de la base de datos")
    except:
        print("Error al cargar base de datos")


# ----------------------------------------------------------
# GENERAR ID
# ----------------------------------------------------------
def generarID():
    if not productos:
        return 1

    try:
        idMayor = max(p.get("id", 0) for p in productos)
        return idMayor + 1
    except:
        return len(productos) + 1