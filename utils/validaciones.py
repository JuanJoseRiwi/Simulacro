

def validator(data):
    datos=input(data)
    while not datos.isnumeric() or int(datos)<=0:
        print("Error no se puede numeros negativos o numero -> 0")
        datos=input(data)
    return int(datos)