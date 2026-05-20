import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from logic.funciones_inventario import agregar_producto


def abrir_agregar_producto():

    ventana_agregar = tk.Toplevel()

    ventana_agregar.title("➕ Agregar Producto")
    ventana_agregar.geometry("760x700")
    ventana_agregar.config(bg="#1a1a1a")
    ventana_agregar.resizable(False, False)


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_agregar,
        text="➕ AGREGAR PRODUCTO",
        font=("Arial", 26, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=20)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_agregar,
        text="Complete la información del nuevo producto",
        font=("Arial", 12),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=5)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_agregar,
        bg="#333333",
        height=2,
        width=500
    )

    linea.pack(pady=10)


    # ================= FRAME PRINCIPAL ================= #

    frame = tk.Frame(
        ventana_agregar,
        bg="#1a1a1a"
    )

    frame.pack(pady=25)


    # ================= LABELS ================= #

    labels = [
        "📦 Categoría",
        "🍾 Código",
        "🥃 Nombre",
        "💰 Precio",
        "📦 Stock"
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
            pady=15,
            sticky="w"
        )


    # ================= COMBOBOX ================= #

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


    # ================= ESTILO ENTRADAS ================= #

    estilo_entry = {
        "font": ("Arial", 12),
        "width": 38,
        "bg": "#2b2b2b",
        "fg": "white",
        "insertbackground": "white",
        "relief": "flat",
        "bd": 8
    }


    # ================= ENTRADAS ================= #

    entrada_codigo = tk.Entry(
        frame,
        **estilo_entry
    )

    entrada_codigo.grid(
        row=1,
        column=1,
        padx=10
    )


    entrada_nombre = tk.Entry(
        frame,
        **estilo_entry
    )

    entrada_nombre.grid(
        row=2,
        column=1,
        padx=10
    )


    entrada_precio = tk.Entry(
        frame,
        **estilo_entry
    )

    entrada_precio.grid(
        row=3,
        column=1,
        padx=10
    )


    entrada_stock = tk.Entry(
        frame,
        **estilo_entry
    )

    entrada_stock.grid(
        row=4,
        column=1,
        padx=10
    )


    # ================= RESULTADO ================= #

    resultado_label = tk.Label(
        ventana_agregar,
        text="",
        font=("Arial", 12, "bold"),
        bg="#1a1a1a"
    )

    resultado_label.pack(pady=15)


    # ================= FUNCION GUARDAR ================= #

    def guardar_producto():

        categoria = combo_categoria.get()

        codigo = entrada_codigo.get().strip()

        nombre = entrada_nombre.get().strip()


        if codigo == "" or nombre == "":

            resultado_label.config(
                text="⚠️ Complete todos los campos",
                fg="#EF5350"
            )

            return


        try:

            precio = int(
                entrada_precio.get()
            )

            stock = int(
                entrada_stock.get()
            )

        except ValueError:

            resultado_label.config(
                text="⚠️ Precio y stock deben ser números",
                fg="#EF5350"
            )

            return


        resultado = agregar_producto(
            categoria,
            codigo,
            nombre,
            precio,
            stock
        )


        if resultado:

            resultado_label.config(
                text="✅ Producto agregado correctamente",
                fg="#66BB6A"
            )


            entrada_codigo.delete(0, tk.END)

            entrada_nombre.delete(0, tk.END)

            entrada_precio.delete(0, tk.END)

            entrada_stock.delete(0, tk.END)

        else:

            resultado_label.config(
                text="⚠️ El código ya existe",
                fg="#EF5350"
            )


    # ================= BOTON GUARDAR ================= #

    btn_guardar = tk.Button(
        ventana_agregar,
        text="💾 Guardar Producto",
        bg="#43A047",
        fg="white",
        activebackground="#66BB6A",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=guardar_producto
    )

    btn_guardar.pack(pady=15)


    # ================= HOVER ================= #

    def entrar_hover(e):

        btn_guardar.config(
            bg="#66BB6A"
        )


    def salir_hover(e):

        btn_guardar.config(
            bg="#43A047"
        )


    btn_guardar.bind(
        "<Enter>",
        entrar_hover
    )

    btn_guardar.bind(
        "<Leave>",
        salir_hover
    )


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_agregar,
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
        command=ventana_agregar.destroy
    )

    btn_cerrar.pack(pady=10)