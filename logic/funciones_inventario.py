from logic.funciones_json import cargar_datos, guardar_datos


# ================= AGREGAR PRODUCTO ================= #

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


    # ================= VALIDAR CODIGO ================= #

    for categoria_actual in datos:

        if categoria_actual == "Faltantes" or categoria_actual == "Ventas":
            continue


        for producto in datos[categoria_actual]:

            if producto["codigo"] == codigo:

                return False


    nuevo_producto = {

        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }


    datos[categoria].append(
        nuevo_producto
    )

    guardar_datos(datos)

    return True


# ================= BUSCAR PRODUCTO ================= #

def buscar_producto(
    nombre_producto="",
    categoria_busqueda=None
):

    datos = cargar_datos()

    resultado = []


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        # ================= FILTRAR CATEGORIA ================= #

        if categoria_busqueda:

            if categoria.lower() != categoria_busqueda.lower():

                continue


        for producto in datos[categoria]:

            if nombre_producto.lower() in producto["nombre"].lower():

                resultado.append({

                    "categoria": categoria,
                    "codigo": producto["codigo"],
                    "nombre": producto["nombre"],
                    "precio": producto["precio"],
                    "stock": producto["stock"]
                })


    return resultado


# ================= ACTUALIZAR STOCK ================= #

def actualizar_stock(
    nombre_producto,
    cantidad
):

    datos = cargar_datos()


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        for producto in datos[categoria]:

            if producto["nombre"].lower() == nombre_producto.lower():

                nuevo_stock = (
                    producto["stock"] +
                    cantidad
                )


                # ================= EVITAR NEGATIVOS ================= #

                if nuevo_stock < 0:

                    return False


                producto["stock"] = nuevo_stock


                # ================= AGREGAR A FALTANTES ================= #

                if producto["stock"] == 0:

                    existe = False


                    for faltante in datos["Faltantes"]:

                        if faltante["nombre"].lower() == nombre_producto.lower():

                            existe = True


                    if not existe:

                        datos["Faltantes"].append({

                            "nombre": producto["nombre"]
                        })


                # ================= ELIMINAR DE FALTANTES ================= #

                else:

                    datos["Faltantes"] = [

                        faltante

                        for faltante in datos["Faltantes"]

                        if faltante["nombre"].lower()
                        != nombre_producto.lower()
                    ]


                guardar_datos(datos)

                return True


    return False


# ================= OBTENER PRODUCTOS POR CATEGORIA ================= #

def obtener_productos_categoria(categoria):

    datos = cargar_datos()

    if categoria in datos:

        return datos[categoria]

    return []


# ================= REGISTRAR VENTA ================= #

def registrar_venta(
    productos_venta
):

    datos = cargar_datos()


    if "Ventas" not in datos:

        datos["Ventas"] = []


    # ================= VALIDAR STOCK ================= #

    for item in productos_venta:

        nombre_producto = item["producto"]

        cantidad = item["cantidad"]


        encontrado = False


        for categoria in datos:

            if categoria == "Faltantes" or categoria == "Ventas":
                continue


            for producto in datos[categoria]:

                if producto["nombre"].lower() == nombre_producto.lower():

                    encontrado = True


                    # ================= STOCK INSUFICIENTE ================= #

                    if producto["stock"] < cantidad:

                        return False


        if not encontrado:

            return False


    # ================= REALIZAR VENTAS ================= #

    for item in productos_venta:

        nombre_producto = item["producto"]

        cantidad = item["cantidad"]


        for categoria in datos:

            if categoria == "Faltantes" or categoria == "Ventas":
                continue


            for producto in datos[categoria]:

                if producto["nombre"].lower() == nombre_producto.lower():

                    producto["stock"] -= cantidad


                    total_venta = (

                        producto["precio"] *
                        cantidad
                    )


                    venta = {

                        "producto": producto["nombre"],
                        "cantidad": cantidad,
                        "precio_unitario": producto["precio"],
                        "total": total_venta
                    }


                    datos["Ventas"].append(
                        venta
                    )


                    # ================= AGREGAR A FALTANTES ================= #

                    if producto["stock"] == 0:

                        existe = False


                        for faltante in datos["Faltantes"]:

                            if faltante["nombre"].lower() == producto["nombre"].lower():

                                existe = True


                        if not existe:

                            datos["Faltantes"].append({

                                "nombre": producto["nombre"]
                            })


                    # ================= ELIMINAR DE FALTANTES ================= #

                    else:

                        datos["Faltantes"] = [

                            faltante

                            for faltante in datos["Faltantes"]

                            if faltante["nombre"].lower()
                            != producto["nombre"].lower()
                        ]


    guardar_datos(datos)

    return True


# ================= OBTENER INVENTARIO ================= #

def obtener_todo_inventario():

    datos = cargar_datos()

    return datos


# ================= OBTENER FALTANTES ================= #

def obtener_faltantes():

    datos = cargar_datos()

    return datos["Faltantes"]


# ================= TOTAL PRODUCTOS ================= #

def total_productos():

    datos = cargar_datos()

    total = 0


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        total += len(
            datos[categoria]
        )


    return total


# ================= TOTAL STOCK ================= #

def total_stock():

    datos = cargar_datos()

    total = 0


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        for producto in datos[categoria]:

            total += producto["stock"]


    return total


# ================= VALOR TOTAL INVENTARIO ================= #

def valor_total_inventario():

    datos = cargar_datos()

    total = 0


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        for producto in datos[categoria]:

            total += (

                producto["precio"] *
                producto["stock"]
            )


    return total


# ================= PRODUCTO MAYOR STOCK ================= #

def producto_mayor_stock():

    datos = cargar_datos()

    mayor = None


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        for producto in datos[categoria]:

            if mayor is None or producto["stock"] > mayor["stock"]:

                mayor = producto


    return mayor


# ================= ELIMINAR PRODUCTO ================= #

def eliminar_producto(nombre_producto):

    datos = cargar_datos()


    for categoria in datos:

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        for producto in datos[categoria]:

            if producto["nombre"].lower() == nombre_producto.lower():

                datos[categoria].remove(
                    producto
                )


                # ================= ELIMINAR DE FALTANTES ================= #

                datos["Faltantes"] = [

                    faltante

                    for faltante in datos["Faltantes"]

                    if faltante["nombre"].lower()
                    != nombre_producto.lower()
                ]


                guardar_datos(datos)

                return True


    return False


# ================= TOTAL VENTAS ================= #

def total_ventas():

    datos = cargar_datos()


    if "Ventas" not in datos:

        return 0


    total = 0


    for venta in datos["Ventas"]:

        total += venta["total"]


    return total


# ================= CANTIDAD VENTAS ================= #

def cantidad_ventas():

    datos = cargar_datos()


    if "Ventas" not in datos:

        return 0


    return len(
        datos["Ventas"]
    )