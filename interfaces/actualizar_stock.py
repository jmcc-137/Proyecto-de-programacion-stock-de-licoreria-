import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from logic.funciones_inventario import (
    actualizar_stock,
    obtener_productos_categoria
)


def abrir_actualizar_stock():

    ventana_stock = tk.Toplevel()

    ventana_stock.title("📦 Actualizar Stock")
    ventana_stock.geometry("760x720")
    ventana_stock.config(bg="#1a1a1a")
    ventana_stock.resizable(False, False)


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_stock,
        text="📦 ACTUALIZAR STOCK",
        font=("Arial", 26, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=20)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_stock,
        text="Agregar unidades al inventario",
        font=("Arial", 12),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=5)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_stock,
        bg="#333333",
        height=2,
        width=500
    )

    linea.pack(pady=10)


    # ================= FRAME PRINCIPAL ================= #

    frame = tk.Frame(
        ventana_stock,
        bg="#1a1a1a"
    )

    frame.pack(pady=25)


    # ================= LABELS ================= #

    labels = [
        "📦 Categoría",
        "🍾 Producto",
        "➕ Cantidad"
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


    # ================= COMBOBOX CATEGORIA ================= #

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


    # ================= COMBOBOX PRODUCTOS ================= #

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
        ventana_stock,
        text="",
        font=("Arial", 12, "bold"),
        bg="#242424",
        fg="white",
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

            texto = (
                f"{producto['nombre']} "
                f"(Stock: {producto['stock']})"
            )

            nombres.append(texto)


        combo_producto["values"] = nombres


        if nombres:

            combo_producto.current(0)

            mostrar_info_producto()


    combo_categoria.bind(
        "<<ComboboxSelected>>",
        actualizar_productos
    )


    # ================= INFO PRODUCTO ================= #

    def mostrar_info_producto(event=None):

        categoria = combo_categoria.get()

        productos = obtener_productos_categoria(categoria)

        nombre = combo_producto.get().split(" (Stock")[0]


        for producto in productos:

            if producto["nombre"] == nombre:

                stock = producto["stock"]


                if stock <= 5:

                    alerta = "\n⚠️ Stock bajo"

                    color = "#EF5350"

                else:

                    alerta = "\n✅ Stock estable"

                    color = "#66BB6A"


                texto = (
                    f"🥃 Producto: {producto['nombre']}\n"
                    f"💰 Precio: ${producto['precio']}\n"
                    f"📦 Stock actual: {stock}"
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


    # ================= ENTRY CANTIDAD ================= #

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


    # ================= RESULTADO ================= #

    resultado_label = tk.Label(
        ventana_stock,
        text="",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a"
    )

    resultado_label.pack(pady=15)


    # ================= FUNCION ACTUALIZAR ================= #

    def actualizar():

        nombre_producto = combo_producto.get().split(" (Stock")[0]


        try:

            cantidad = int(
                entrada_cantidad.get()
            )

        except ValueError:

            resultado_label.config(
                text="⚠️ La cantidad debe ser numérica",
                fg="#EF5350"
            )

            return


        resultado = actualizar_stock(
            nombre_producto,
            cantidad
        )


        if resultado:

            resultado_label.config(
                text="✅ Stock actualizado correctamente",
                fg="#66BB6A"
            )

            entrada_cantidad.delete(0, tk.END)

            actualizar_productos()

        else:

            resultado_label.config(
                text="❌ Error al actualizar stock",
                fg="#EF5350"
            )


    # ================= BOTON ACTUALIZAR ================= #

    btn_actualizar = tk.Button(
        ventana_stock,
        text="📦 Actualizar Stock",
        bg="#00ACC1",
        fg="white",
        activebackground="#26C6DA",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=actualizar
    )

    btn_actualizar.pack(pady=15)


    # ================= HOVER ================= #

    def entrar_hover(e):

        btn_actualizar.config(
            bg="#26C6DA"
        )


    def salir_hover(e):

        btn_actualizar.config(
            bg="#00ACC1"
        )


    btn_actualizar.bind(
        "<Enter>",
        entrar_hover
    )

    btn_actualizar.bind(
        "<Leave>",
        salir_hover
    )


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_stock,
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
        command=ventana_stock.destroy
    )

    btn_cerrar.pack(pady=10)