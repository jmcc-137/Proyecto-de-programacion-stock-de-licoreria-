import tkinter as tk
from tkinter import ttk

from logic.funciones_inventario import (
    total_productos,
    total_stock,
    valor_total_inventario,
    producto_mayor_stock,
    total_ventas,
    cantidad_ventas
)

from logic.funciones_json import cargar_datos


def abrir_estadisticas():

    ventana_estadisticas = tk.Toplevel()

    ventana_estadisticas.title("📊 Estadísticas")
    ventana_estadisticas.geometry("960x860")
    ventana_estadisticas.config(bg="#121212")
    ventana_estadisticas.resizable(False, False)


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_estadisticas,
        text="📊 ESTADÍSTICAS DEL SISTEMA",
        font=("Arial", 24, "bold"),
        bg="#121212",
        fg="white"
    )

    titulo.pack(pady=15)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_estadisticas,
        text="Resumen general del inventario y ventas",
        font=("Arial", 11),
        bg="#121212",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=3)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_estadisticas,
        bg="#333333",
        height=2,
        width=550
    )

    linea.pack(pady=10)


    # ================= DATOS ================= #

    producto_top = producto_mayor_stock()


    estadisticas = [

        (
            "🍾 Total de productos",
            total_productos(),
            "#42A5F5"
        ),

        (
            "📦 Total de unidades",
            total_stock(),
            "#66BB6A"
        ),

        (
            "💰 Valor total inventario",
            f"${valor_total_inventario()}",
            "#FFCA28"
        ),

        (
            "🏆 Producto con más stock",
            producto_top['nombre'],
            "#AB47BC"
        ),

        (
            "📈 Stock más alto",
            producto_top['stock'],
            "#26C6DA"
        ),

        (
            "🛒 Ventas realizadas",
            cantidad_ventas(),
            "#EF5350"
        ),

        (
            "💵 Total vendido",
            f"${total_ventas()}",
            "#FFA726"
        )
    ]


    # ================= FRAME PRINCIPAL ================= #

    frame = tk.Frame(
        ventana_estadisticas,
        bg="#121212"
    )

    frame.pack(pady=15)


    # ================= TARJETAS ================= #

    for titulo_card, valor, color in estadisticas:

        card = tk.Frame(
            frame,
            bg="#1E1E1E",
            width=600,
            height=60,
            highlightbackground=color,
            highlightthickness=2
        )

        card.pack(
            pady=6
        )

        card.pack_propagate(False)


        label_titulo = tk.Label(
            card,
            text=titulo_card,
            font=("Arial", 11, "bold"),
            bg="#1E1E1E",
            fg="white"
        )

        label_titulo.pack(
            pady=(6, 0)
        )


        label_valor = tk.Label(
            card,
            text=valor,
            font=("Arial", 15, "bold"),
            bg="#1E1E1E",
            fg=color
        )

        label_valor.pack(
            pady=(0, 6)
        )


    # ================= VER VENTAS ================= #

    def ver_ventas():

        ventana_ventas = tk.Toplevel()

        ventana_ventas.title("🛒 Ventas Detalladas")
        ventana_ventas.geometry("950x780")
        ventana_ventas.config(bg="#121212")
        ventana_ventas.resizable(False, False)


        # ================= ESTILOS ================= #

        estilo = ttk.Style()

        estilo.theme_use("clam")


        estilo.configure(

            "Treeview",

            background="#1E1E1E",
            foreground="white",
            fieldbackground="#1E1E1E",
            rowheight=35,
            borderwidth=0,
            font=("Arial", 10)
        )


        estilo.configure(

            "Treeview.Heading",

            background="#2962FF",
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
            ventana_ventas,
            text="🛒 VENTAS DETALLADAS",
            font=("Arial", 28, "bold"),
            bg="#121212",
            fg="white"
        )

        titulo.pack(pady=15)


        # ================= RESUMEN ================= #

        resumen_frame = tk.Frame(
            ventana_ventas,
            bg="#121212"
        )

        resumen_frame.pack(pady=5)


        # CARD TOTAL VENDIDO

        card1 = tk.Frame(
            resumen_frame,
            bg="#1E88E5",
            width=240,
            height=80
        )

        card1.grid(
            row=0,
            column=0,
            padx=10
        )

        card1.pack_propagate(False)


        label1 = tk.Label(
            card1,
            text="💰 TOTAL VENDIDO",
            font=("Arial", 11, "bold"),
            bg="#1E88E5",
            fg="white"
        )

        label1.pack(pady=(10, 0))


        valor1 = tk.Label(
            card1,
            text=f"${total_ventas()}",
            font=("Arial", 18, "bold"),
            bg="#1E88E5",
            fg="white"
        )

        valor1.pack()


        # CARD TOTAL VENTAS

        card2 = tk.Frame(
            resumen_frame,
            bg="#43A047",
            width=240,
            height=80
        )

        card2.grid(
            row=0,
            column=1,
            padx=10
        )

        card2.pack_propagate(False)


        label2 = tk.Label(
            card2,
            text="🛒 TOTAL VENTAS",
            font=("Arial", 11, "bold"),
            bg="#43A047",
            fg="white"
        )

        label2.pack(pady=(10, 0))


        valor2 = tk.Label(
            card2,
            text=cantidad_ventas(),
            font=("Arial", 18, "bold"),
            bg="#43A047",
            fg="white"
        )

        valor2.pack()


        # ================= FRAME TABLA ================= #

        frame_tabla = tk.Frame(
            ventana_ventas,
            bg="#121212"
        )

        frame_tabla.pack(
            pady=20,
            padx=20,
            fill="both",
            expand=True
        )


        # ================= SCROLL ================= #

        scroll = tk.Scrollbar(
            frame_tabla
        )

        scroll.pack(
            side="right",
            fill="y"
        )


        # ================= TABLA ================= #

        columnas = (
            "producto",
            "cantidad",
            "total",
            "stock"
        )


        tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=12,
            yscrollcommand=scroll.set
        )


        # ================= HEADINGS ================= #

        tabla.heading(
            "producto",
            text="🍾 Producto"
        )

        tabla.heading(
            "cantidad",
            text="📦 Cantidad"
        )

        tabla.heading(
            "total",
            text="💰 Total"
        )

        tabla.heading(
            "stock",
            text="📈 Stock Actual"
        )


        # ================= COLUMNAS ================= #

        tabla.column(
            "producto",
            width=260,
            anchor="center"
        )

        tabla.column(
            "cantidad",
            width=180,
            anchor="center"
        )

        tabla.column(
            "total",
            width=180,
            anchor="center"
        )

        tabla.column(
            "stock",
            width=180,
            anchor="center"
        )


        tabla.pack(
            side="left",
            fill="both",
            expand=True
        )


        scroll.config(
            command=tabla.yview
        )


        # ================= FILAS COLORES ================= #

        tabla.tag_configure(
            "par",
            background="#1E1E1E"
        )

        tabla.tag_configure(
            "impar",
            background="#2A2A2A"
        )


        # ================= CARGAR DATOS ================= #

        datos = cargar_datos()

        ventas = datos["Ventas"]


        for i, venta in enumerate(ventas):

            stock_actual = "No encontrado"


            for categoria in datos:

                if categoria == "Ventas" or categoria == "Faltantes":
                    continue

                for producto in datos[categoria]:

                    if producto["nombre"] == venta["producto"]:

                        stock_actual = producto["stock"]


            tag = "par"

            if i % 2 == 0:

                tag = "impar"


            tabla.insert(
                "",
                tk.END,
                values=(
                    venta["producto"],
                    venta["cantidad"],
                    f"${venta['total']}",
                    stock_actual
                ),
                tags=(tag,)
            )


        # ================= BOTON CERRAR ================= #

        btn_cerrar_ventas = tk.Button(
            ventana_ventas,
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
            command=ventana_ventas.destroy
        )

        btn_cerrar_ventas.pack(pady=15)


    # ================= BOTON VER VENTAS ================= #

    btn_ver_ventas = tk.Button(
        ventana_estadisticas,
        text="🛒 Ver Ventas Detalladas",
        bg="#3949AB",
        fg="white",
        activebackground="#5C6BC0",
        activeforeground="white",
        font=("Arial", 11, "bold"),
        width=25,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=ver_ventas
    )

    btn_ver_ventas.pack(pady=10)


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_estadisticas,
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
        command=ventana_estadisticas.destroy
    )

    btn_cerrar.pack(pady=15)