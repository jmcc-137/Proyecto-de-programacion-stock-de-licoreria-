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

    resultado = []

    for categoria in datos:

        if categoria == "Faltantes":
            continue

        for producto in datos[categoria]:

            if  nombre_producto.lower() in producto["nombre"].lower():
                resultado.append(producto)

    return resultado

def actualizar_stock(nombre_producto, cantidad):

    datos = cargar_datos()


    for categoria in datos:

        if categoria == "Faltantes":
            continue


        for producto in datos[categoria]:

            if producto["nombre"].lower() == nombre_producto.lower():

                producto["stock"] += cantidad


                # ================= ELIMINAR DE FALTANTES ================= #

                if producto["stock"] > 0:

                    datos["Faltantes"] = [

                        faltante

                        for faltante in datos["Faltantes"]

                        if faltante["nombre"].lower()
                        != nombre_producto.lower()
                    ]


                guardar_datos(datos)

                return True


    return False
def obtener_productos_categoria(categoria):
    datos = cargar_datos()
    if categoria in datos:
        return datos[categoria]
    return []

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

def obtener_todo_inventario():
    datos = cargar_datos()
    return datos
            
def obtener_faltantes():
    datos = cargar_datos()
    return datos["Faltantes"]

def total_productos():
    datos = cargar_datos()
    total = 0
    for categoria in datos:
        if categoria == "Faltantes":
            continue
        total += len(datos[categoria])
    return total
def total_stock():

    datos = cargar_datos()

    total = 0


    for categoria in datos:

        if categoria == "Faltantes":
            continue


        for producto in datos[categoria]:

            total += producto["stock"]


    return total
def valor_total_inventario():

    datos = cargar_datos()

    total = 0


    for categoria in datos:

        if categoria == "Faltantes":
            continue


        for producto in datos[categoria]:

            total += (
                producto["precio"] *
                producto["stock"]
            )


    return total
        
def producto_mayor_stock():

    datos = cargar_datos()

    mayor = None


    for categoria in datos:

        if categoria == "Faltantes":
            continue


        for producto in datos[categoria]:

            if mayor is None or producto["stock"] > mayor["stock"]:

                mayor = producto


    return mayor
def eliminar_producto(nombre_producto):

    datos = cargar_datos()


    for categoria in datos:

        if categoria == "Faltantes":
            continue


        for producto in datos[categoria]:

            if producto["nombre"].lower() == nombre_producto.lower():

                datos[categoria].remove(producto)

                guardar_datos(datos)

                return True


    return False