import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from logic.funciones_inventario import (
    eliminar_producto,
    obtener_productos_categoria
)


def abrir_eliminar_producto():

    ventana_eliminar = tk.Toplevel()

    ventana_eliminar.title("❌ Eliminar Producto")
    ventana_eliminar.geometry("760x650")
    ventana_eliminar.config(bg="#1a1a1a")
    ventana_eliminar.resizable(False, False)


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_eliminar,
        text="❌ ELIMINAR PRODUCTO",
        font=("Arial", 24, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=18)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_eliminar,
        text="Seleccione un producto para eliminar",
        font=("Arial", 11),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=4)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_eliminar,
        bg="#333333",
        height=2,
        width=450
    )

    linea.pack(pady=8)


    # ================= FRAME PRINCIPAL ================= #

    frame = tk.Frame(
        ventana_eliminar,
        bg="#1a1a1a"
    )

    frame.pack(pady=20)


    # ================= LABELS ================= #

    labels = [
        "📦 Categoría",
        "🍾 Producto"
    ]


    for i, texto in enumerate(labels):

        label = tk.Label(
            frame,
            text=texto,
            font=("Arial", 12, "bold"),
            bg="#1a1a1a",
            fg="white"
        )

        label.grid(
            row=i,
            column=0,
            padx=15,
            pady=18,
            sticky="w"
        )


    # ================= CATEGORIAS ================= #

    categorias = [
        "Cervezas",
        "Whisky",
        "Vinos",
        "Ron",
        "Vodka",
        "Tequila"
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


    # ================= PRODUCTOS ================= #

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


    # ================= PANEL PRODUCTO ================= #

    info_producto = tk.Label(
        ventana_eliminar,
        text="",
        font=("Arial", 12, "bold"),
        bg="#242424",
        fg="#EF5350",
        width=45,
        height=4,
        justify="left"
    )

    info_producto.pack(pady=15)


    # ================= ACTUALIZAR PRODUCTOS ================= #

    def actualizar_productos(event=None):

        categoria = combo_categoria.get()

        productos = obtener_productos_categoria(categoria)

        nombres = []


        for producto in productos:

            nombres.append(
                producto["nombre"]
            )


        combo_producto["values"] = nombres


        if nombres:

            combo_producto.current(0)

            mostrar_info_producto()


    combo_categoria.bind(
        "<<ComboboxSelected>>",
        actualizar_productos
    )


    # ================= MOSTRAR INFO ================= #

    def mostrar_info_producto(event=None):

        categoria = combo_categoria.get()

        productos = obtener_productos_categoria(categoria)

        nombre = combo_producto.get()


        for producto in productos:

            if producto["nombre"] == nombre:

                texto = (
                    f"🥃 Producto: {producto['nombre']}\n"
                    f"💰 Precio: ${producto['precio']}\n"
                    f"📦 Stock actual: {producto['stock']}"
                )

                info_producto.config(
                    text=texto
                )


    combo_producto.bind(
        "<<ComboboxSelected>>",
        mostrar_info_producto
    )


    actualizar_productos()


    # ================= RESULTADO ================= #

    resultado_label = tk.Label(
        ventana_eliminar,
        text="",
        font=("Arial", 11, "bold"),
        bg="#1a1a1a"
    )

    resultado_label.pack(pady=12)


    # ================= FUNCION ELIMINAR ================= #

    def eliminar():

        nombre_producto = combo_producto.get()


        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que deseas eliminar\n\n{nombre_producto}?"
        )


        if confirmar:

            resultado = eliminar_producto(
                nombre_producto
            )


            if resultado:

                resultado_label.config(
                    text="✅ Producto eliminado correctamente",
                    fg="#66BB6A"
                )

                actualizar_productos()

            else:

                resultado_label.config(
                    text="❌ Error al eliminar producto",
                    fg="#EF5350"
                )


    # ================= BOTON ELIMINAR ================= #

    btn_eliminar = tk.Button(
        ventana_eliminar,
        text="🗑️ Eliminar Producto",
        bg="#E53935",
        fg="white",
        activebackground="#EF5350",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=24,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=eliminar
    )

    btn_eliminar.pack(pady=10)


    # ================= HOVER ================= #

    def entrar_hover(e):

        btn_eliminar.config(
            bg="#EF5350"
        )


    def salir_hover(e):

        btn_eliminar.config(
            bg="#E53935"
        )


    btn_eliminar.bind(
        "<Enter>",
        entrar_hover
    )

    btn_eliminar.bind(
        "<Leave>",
        salir_hover
    )


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_eliminar,
        text="❌ Cerrar",
        bg="#C62828",
        fg="white",
        activebackground="#E53935",
        activeforeground="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=ventana_eliminar.destroy
    )

    btn_cerrar.pack(pady=12)