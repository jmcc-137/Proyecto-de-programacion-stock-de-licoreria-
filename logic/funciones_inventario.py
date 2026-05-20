from logic.funciones_json import cargar_datos, guardar_datos


def agregar_producto(
    categoria,
    codigo,
    nombre,
    precio,
    stock
):


    datos = cargar_datos()
    
    if categoria not in datos:
        datos[categoria] = []
    
    for producto in datos[categoria]:
        if producto["codigo"] == codigo:
            return False

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    datos[categoria].append(nuevo_producto)

    guardar_datos(datos)

    return True


def buscar_producto(nombre_producto):

    datos = cargar_datos()

    for categoria in datos:

        if categoria == "Faltantes":
            continue

        for producto in datos[categoria]:

            if producto["nombre"].lower() == nombre_producto.lower():

                return producto

    return None

def actualizar_stock(nombre_producto, cantidad):
    datos = cargar_datos()
    for categoria in datos:
        if categoria == "Faltantes":
            continue
        for producto in datos[categoria]:
            if producto["nombre"].lower()== nombre_producto.lower():
                producto["stock"] += cantidad
                guardar_datos(datos)
                return True
    return False

def registrar_venta(nombre_producto, cantidad):

    datos = cargar_datos()

    for categoria in datos:

        if categoria == "Faltantes":
            continue

        for producto in datos[categoria]:

            if producto["nombre"].lower() == nombre_producto.lower():

                if producto["stock"] >= cantidad:

                    producto["stock"] -= cantidad

                    if producto["stock"] == 0:

                        datos["Faltantes"].append({
                            "nombre": producto["nombre"]
                        })

                    guardar_datos(datos)

                    return True

                else:

                    return False

    return False
            
        