import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from logic.funciones_inventario import (
    registrar_venta,
    obtener_productos_categoria
)


def abrir_ventas():

    ventana_ventas = tk.Toplevel()

    ventana_ventas.title("💰 Registrar Venta")
    ventana_ventas.geometry("980x760")
    ventana_ventas.config(bg="#1a1a1a")
    ventana_ventas.resizable(False, False)


    # ================= VARIABLES ================= #

    carrito = []


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_ventas,
        text="💰 REGISTRAR VENTA",
        font=("Arial", 26, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=12)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_ventas,
        text="Agrega productos al carrito de ventas",
        font=("Arial", 12),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=2)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_ventas,
        bg="#333333",
        height=2,
        width=500
    )

    linea.pack(pady=8)


    # ================= FRAME PRINCIPAL ================= #

    frame = tk.Frame(
        ventana_ventas,
        bg="#1a1a1a"
    )

    frame.pack(pady=8)


    # ================= CATEGORIA ================= #

    label_categoria = tk.Label(
        frame,
        text="📦 Categoría",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    label_categoria.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )


    categorias = [
        "Cervezas",
        "Whisky",
        "Vinos",
        "Ron",
        "Vodka",
        "Tequila",
        "Aguardiente"
    ]


    combo_categoria = ttk.Combobox(
        frame,
        values=categorias,
        state="readonly",
        width=35,
        font=("Arial", 11)
    )

    combo_categoria.grid(
        row=0,
        column=1,
        padx=10
    )

    combo_categoria.current(0)


    # ================= PRODUCTO ================= #

    label_producto = tk.Label(
        frame,
        text="🍾 Producto",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    label_producto.grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )


    combo_producto = ttk.Combobox(
        frame,
        state="readonly",
        width=35,
        font=("Arial", 11)
    )

    combo_producto.grid(
        row=1,
        column=1,
        padx=10
    )


    # ================= CANTIDAD ================= #

    label_cantidad = tk.Label(
        frame,
        text="📦 Cantidad",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    label_cantidad.grid(
        row=2,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )


    entrada_cantidad = tk.Entry(
        frame,
        font=("Arial", 12),
        width=38,
        bg="#2b2b2b",
        fg="white",
        insertbackground="white",
        relief="flat",
        bd=8
    )

    entrada_cantidad.grid(
        row=2,
        column=1,
        padx=10
    )


    # ================= INFO PRODUCTO ================= #

    info_producto = tk.Label(
        ventana_ventas,
        text="",
        font=("Arial", 11, "bold"),
        bg="#242424",
        fg="white",
        width=45,
        height=4,
        justify="left"
    )

    info_producto.pack(pady=8)


    # ================= ACTUALIZAR PRODUCTOS ================= #

    def actualizar_productos(event=None):

        categoria = combo_categoria.get()

        productos = obtener_productos_categoria(
            categoria
        )

        nombres_productos = []


        for producto in productos:

            texto_producto = (
                f"{producto['nombre']} "
                f"(Stock: {producto['stock']})"
            )

            nombres_productos.append(
                texto_producto
            )


        combo_producto["values"] = nombres_productos


        if nombres_productos:

            combo_producto.current(0)

            mostrar_info_producto()


    combo_categoria.bind(
        "<<ComboboxSelected>>",
        actualizar_productos
    )


    # ================= MOSTRAR INFO ================= #

    def mostrar_info_producto(event=None):

        categoria = combo_categoria.get()

        productos = obtener_productos_categoria(
            categoria
        )

        nombre = combo_producto.get().split(
            " (Stock"
        )[0]


        for producto in productos:

            if producto["nombre"] == nombre:

                stock = producto["stock"]


                if stock <= 5:

                    alerta = "\n⚠️ Stock bajo"

                    color = "#EF5350"

                elif stock <= 15:

                    alerta = "\n📦 Stock medio"

                    color = "#FFD54F"

                else:

                    alerta = "\n✅ Stock disponible"

                    color = "#66BB6A"


                texto = (
                    f"🥃 Producto: {producto['nombre']}\n"
                    f"💰 Precio: ${producto['precio']}\n"
                    f"📦 Stock disponible: {stock}"
                    f"{alerta}"
                )

                info_producto.config(
                    text=texto,
                    fg=color
                )


    combo_producto.bind(
        "<<ComboboxSelected>>",
        mostrar_info_producto
    )


    actualizar_productos()


    # ================= FRAME CARRITO ================= #

    frame_carrito = tk.Frame(
        ventana_ventas,
        bg="#1a1a1a"
    )

    frame_carrito.pack(
        pady=10
    )


    # ================= SCROLL TABLA ================= #

    scroll = tk.Scrollbar(
        frame_carrito
    )

    scroll.pack(
        side="right",
        fill="y"
    )


    # ================= TABLA ================= #

    columnas = (
        "producto",
        "cantidad"
    )


    tabla = ttk.Treeview(

        frame_carrito,

        columns=columnas,
        show="headings",
        height=6,
        yscrollcommand=scroll.set
    )


    tabla.heading(
        "producto",
        text="🍾 Producto"
    )

    tabla.heading(
        "cantidad",
        text="📦 Cantidad"
    )


    tabla.column(
        "producto",
        width=420,
        anchor="center"
    )

    tabla.column(
        "cantidad",
        width=180,
        anchor="center"
    )


    tabla.pack()


    scroll.config(
        command=tabla.yview
    )


    # ================= TOTAL ================= #

    total_label = tk.Label(
        ventana_ventas,
        text="💰 TOTAL PRODUCTOS: 0",
        font=("Arial", 14, "bold"),
        bg="#1a1a1a",
        fg="#66BB6A"
    )

    total_label.pack(pady=6)


    # ================= ACTUALIZAR TOTAL ================= #

    def actualizar_total():

        total = 0


        for item in carrito:

            total += item["cantidad"]


        total_label.config(
            text=f"💰 TOTAL PRODUCTOS: {total}"
        )


    # ================= AGREGAR CARRITO ================= #

    def agregar_carrito():

        if combo_producto.get() == "":

            messagebox.showwarning(
                "Advertencia",
                "⚠️ Selecciona un producto"
            )

            return


        try:

            cantidad = int(
                entrada_cantidad.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "⚠️ Cantidad inválida"
            )

            return


        if cantidad <= 0:

            messagebox.showwarning(
                "Advertencia",
                "⚠️ La cantidad debe ser mayor a 0"
            )

            return


        nombre_producto = combo_producto.get().split(
            " (Stock"
        )[0]


        carrito.append({

            "producto": nombre_producto,
            "cantidad": cantidad
        })


        tabla.insert(
            "",
            tk.END,
            values=(
                nombre_producto,
                cantidad
            )
        )


        entrada_cantidad.delete(
            0,
            tk.END
        )

        actualizar_total()


    # ================= ELIMINAR CARRITO ================= #

    def eliminar_producto_carrito():

        seleccion = tabla.selection()


        if not seleccion:

            return


        index = tabla.index(
            seleccion[0]
        )


        tabla.delete(
            seleccion[0]
        )

        carrito.pop(index)

        actualizar_total()


    # ================= REGISTRAR VENTA ================= #

    def vender_productos():

        if len(carrito) == 0:

            messagebox.showwarning(
                "Advertencia",
                "⚠️ El carrito está vacío"
            )

            return


        resultado = registrar_venta(
            carrito
        )


        if resultado:

            messagebox.showinfo(
                "Éxito",
                "✅ Venta registrada correctamente"
            )


            carrito.clear()


            for item in tabla.get_children():

                tabla.delete(item)


            actualizar_total()

            actualizar_productos()

        else:

            messagebox.showerror(
                "Error",
                "❌ Stock insuficiente"
            )


    # ================= BOTONES ================= #

    frame_botones = tk.Frame(
        ventana_ventas,
        bg="#1a1a1a"
    )

    frame_botones.pack(pady=8)


    # BOTON AGREGAR

    btn_agregar = tk.Button(
        frame_botones,
        text="🛒 Agregar al Carrito",
        bg="#1E88E5",
        fg="white",
        font=("Arial", 11, "bold"),
        width=22,
        height=2,
        relief="flat",
        cursor="hand2",
        command=agregar_carrito
    )

    btn_agregar.grid(
        row=0,
        column=0,
        padx=10
    )


    # BOTON ELIMINAR

    btn_eliminar = tk.Button(
        frame_botones,
        text="🗑️ Eliminar",
        bg="#EF5350",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        relief="flat",
        cursor="hand2",
        command=eliminar_producto_carrito
    )

    btn_eliminar.grid(
        row=0,
        column=1,
        padx=10
    )


    # BOTON VENDER

    btn_vender = tk.Button(
        ventana_ventas,
        text="💸 Registrar Venta",
        bg="#8E24AA",
        fg="white",
        activebackground="#BA68C8",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=28,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=vender_productos
    )

    btn_vender.pack(pady=6)


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_ventas,
        text="❌ Cerrar",
        bg="#C62828",
        fg="white",
        activebackground="#E53935",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=ventana_ventas.destroy
    )

    btn_cerrar.pack(pady=8)