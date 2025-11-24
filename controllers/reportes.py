import json
import tabulate 
import models.data as db

archivo="reporteIngresos.json"

def reporteVentasPorMarca():

    ventasPormarca = db.ventas

    if not ventasPormarca:
        print("No hay ventas registradas")
        return
    
    conteo = {}

    
    for v in ventasPormarca:
        marca = v.get("marca", "Desconocida")
        cantidad = v.get("cantidad", 0)
        conteo[marca] = conteo.get(marca, 0) + cantidad

    # Ordenamos de mayor a menor cantidad vendida
    top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

    tabla = []
    for marca, cant in top3:
        tabla.append([marca, cant])

    print(tabulate.tabulate(
        tabla,
        headers=["Marca", "Cantidad Vendida"],
        tablefmt="grid"
    ))

def reporteTop3():

    ventasPormarca=db.ventas

    if not ventasPormarca:
        print("No hay ventas registradas")
        return
    
    conteo={}

    for x in ventasPormarca:
        productos=x.get("producto","")
        cantidad=x.get("cantidad",0)
        conteo[productos]=conteo.get(productos,0)+cantidad

    top3=sorted(conteo.items(),key=lambda x:x[1],reverse=True)[:3]

    tabla=[]


    for product,cant in top3:
        tabla.append([product,cant])

    print(tabulate.tabulate(
        tabla,
        headers=["Producto","Cantidad Vendida"],
        tablefmt="grid"
    ))


def reporteIngresos():
  
    ventas=db.ventas
    
    if not ventas:
        print("No hay ventas registradas")
        return
    
    ingresoBruto=sum(x["total"] for x in ventas)
    ingresoNeto=ingresoBruto*0.90

    bruto = f"{ingresoBruto:,.0f}".replace(",", ".")
    neto = f"{ingresoNeto:,.0f}".replace(",", ".")

    tabla=[["Ingreso Bruto",bruto],
           ["Ingreso Neto (90%)",neto] 
           ]
    
    print(tabulate.tabulate(tabla,headers=["Detalle","Valores"],tablefmt="grid"))

    reporte={
        "fecha":db.fechas(),
        "Ingreso Bruto":ingresoBruto,
        "Ingreso Neto":ingresoNeto
    }

    try:
        with open(archivo,"r",encoding="utf-8") as file:
            r=json.load(file)
    except:
        r=[]

    r.append(reporte)

    with open(archivo,"w",encoding="utf-8") as file:
        json.dump(r,file,indent=4,ensure_ascii=False)
    print("Se guardo con exito")