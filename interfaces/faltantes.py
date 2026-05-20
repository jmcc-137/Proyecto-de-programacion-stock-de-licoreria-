import tkinter as tk
from tkinter import ttk

from logic.funciones_inventario import obtener_faltantes


def abrir_faltantes():

    ventana_faltantes = tk.Toplevel()

    ventana_faltantes.title("⚠️ Productos Faltantes")
    ventana_faltantes.geometry("720x580")
    ventana_faltantes.config(bg="#1a1a1a")
    ventana_faltantes.resizable(False, False)


    # ================= ESTILOS ================= #

    estilo = ttk.Style()

    estilo.theme_use("clam")


    estilo.configure(
        "Treeview",
        background="#242424",
        foreground="white",
        rowheight=30,
        fieldbackground="#242424",
        borderwidth=0,
        font=("Arial", 10)
    )


    estilo.configure(
        "Treeview.Heading",
        background="#333333",
        foreground="white",
        font=("Arial", 11, "bold"),
        relief="flat"
    )


    estilo.map(
        "Treeview",
        background=[("selected", "#EF5350")]
    )


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_faltantes,
        text="⚠️ PRODUCTOS FALTANTES",
        font=("Arial", 22, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=15)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_faltantes,
        text="Productos agotados o sin stock",
        font=("Arial", 11),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=3)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_faltantes,
        bg="#333333",
        height=2,
        width=450
    )

    linea.pack(pady=8)


    # ================= DATOS ================= #

    faltantes = obtener_faltantes()


    # ================= CONTADOR ================= #

    contador = tk.Label(
        ventana_faltantes,
        text=f"⚠️ Productos agotados: {len(faltantes)}",
        font=("Arial", 11, "bold"),
        bg="#1a1a1a",
        fg="#EF5350"
    )

    contador.pack(pady=8)


    # ================= FRAME TABLA ================= #

    frame_tabla = tk.Frame(
        ventana_faltantes,
        bg="#1a1a1a"
    )

    frame_tabla.pack(
        pady=5
    )


    # ================= SCROLL ================= #

    scroll = tk.Scrollbar(
        frame_tabla,
        orient="vertical"
    )

    scroll.pack(
        side="right",
        fill="y"
    )


    # ================= TABLA ================= #

    columnas = (
        "nombre",
    )


    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        yscrollcommand=scroll.set,
        height=8
    )


    tabla.heading(
        "nombre",
        text="🍾 Producto Agotado"
    )


    tabla.column(
        "nombre",
        width=520,
        anchor="center"
    )


    tabla.pack(
        side="left"
    )


    scroll.config(
        command=tabla.yview
    )


    # ================= INSERTAR DATOS ================= #

    if faltantes:

        for producto in faltantes:

            tabla.insert(
                "",
                tk.END,
                values=(
                    producto["nombre"],
                )
            )

    else:

        tabla.insert(
            "",
            tk.END,
            values=(
                "✅ No hay productos faltantes",
            )
        )


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_faltantes,
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
        command=ventana_faltantes.destroy
    )

    btn_cerrar.pack(pady=12)


    # ================= HOVER ================= #

    def entrar_hover(e):

        btn_cerrar.config(
            bg="#E53935"
        )


    def salir_hover(e):

        btn_cerrar.config(
            bg="#C62828"
        )


    btn_cerrar.bind(
        "<Enter>",
        entrar_hover
    )

    btn_cerrar.bind(
        "<Leave>",
        salir_hover
    )