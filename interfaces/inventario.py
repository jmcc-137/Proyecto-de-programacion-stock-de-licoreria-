import tkinter as tk
from tkinter import ttk

from logic.funciones_inventario import obtener_todo_inventario


def abrir_inventario():

    ventana_inventario = tk.Toplevel()

    ventana_inventario.title("📦 Inventario")
    ventana_inventario.geometry("980x720")
    ventana_inventario.config(bg="#1a1a1a")
    ventana_inventario.resizable(False, False)


    # ================= ESTILOS ================= #

    estilo = ttk.Style()

    estilo.theme_use("clam")


    estilo.configure(
        "Treeview",
        background="#242424",
        foreground="white",
        rowheight=28,
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
        background=[("selected", "#3949AB")]
    )


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_inventario,
        text="📦 INVENTARIO DE LICORES",
        font=("Arial", 24, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=20)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_inventario,
        text="Visualización completa del inventario",
        font=("Arial", 12),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=5)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_inventario,
        bg="#333333",
        height=2,
        width=500
    )

    linea.pack(pady=10)


    # ================= FRAME TABLA ================= #

    frame_tabla = tk.Frame(
        ventana_inventario,
        bg="#1a1a1a"
    )

    frame_tabla.pack(
        pady=10,
        padx=20
    )


    # ================= SCROLL VERTICAL ================= #

    scroll_y = tk.Scrollbar(
        frame_tabla,
        orient="vertical"
    )

    scroll_y.pack(
        side="right",
        fill="y"
    )


    # ================= SCROLL HORIZONTAL ================= #

    scroll_x = tk.Scrollbar(
        frame_tabla,
        orient="horizontal"
    )

    scroll_x.pack(
        side="bottom",
        fill="x"
    )


    # ================= COLUMNAS ================= #

    columnas = (
        "categoria",
        "codigo",
        "nombre",
        "precio",
        "stock"
    )


    # ================= TABLA ================= #

    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=13,
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )


    # ================= ENCABEZADOS ================= #

    tabla.heading("categoria", text="📦 Categoría")
    tabla.heading("codigo", text="🍾 Código")
    tabla.heading("nombre", text="🥃 Producto")
    tabla.heading("precio", text="💰 Precio")
    tabla.heading("stock", text="📦 Stock")


    # ================= TAMAÑO COLUMNAS ================= #

    tabla.column(
        "categoria",
        width=160,
        anchor="center"
    )

    tabla.column(
        "codigo",
        width=120,
        anchor="center"
    )

    tabla.column(
        "nombre",
        width=280,
        anchor="center"
    )

    tabla.column(
        "precio",
        width=150,
        anchor="center"
    )

    tabla.column(
        "stock",
        width=100,
        anchor="center"
    )


    tabla.pack(
        side="left"
    )


    # ================= CONFIGURAR SCROLL ================= #

    scroll_y.config(
        command=tabla.yview
    )

    scroll_x.config(
        command=tabla.xview
    )


    # ================= COLORES STOCK ================= #

    tabla.tag_configure(
        "stock_bajo",
        foreground="#EF5350"
    )

    tabla.tag_configure(
        "stock_medio",
        foreground="#FFD54F"
    )

    tabla.tag_configure(
        "stock_alto",
        foreground="#66BB6A"
    )


    # ================= CARGAR INVENTARIO ================= #

    datos = obtener_todo_inventario()


    for categoria in datos:

        # 🔥 IGNORAR TABLAS ESPECIALES

        if categoria == "Faltantes" or categoria == "Ventas":
            continue


        for producto in datos[categoria]:

            stock = producto["stock"]


            # ================= COLOR SEGUN STOCK ================= #

            if stock <= 5:

                tag = "stock_bajo"

            elif stock <= 15:

                tag = "stock_medio"

            else:

                tag = "stock_alto"


            tabla.insert(
                "",
                tk.END,
                values=(
                    categoria,
                    producto["codigo"],
                    producto["nombre"],
                    f"${producto['precio']}",
                    stock
                ),
                tags=(tag,)
            )


    # ================= FRAME BOTON ================= #

    frame_boton = tk.Frame(
        ventana_inventario,
        bg="#1a1a1a"
    )

    frame_boton.pack(
        pady=15
    )


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        frame_boton,
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
        command=ventana_inventario.destroy
    )

    btn_cerrar.pack()