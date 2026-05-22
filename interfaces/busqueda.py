import tkinter as tk
from tkinter import ttk

from logic.funciones_inventario import buscar_producto


def abrir_busqueda():

    ventana_busqueda = tk.Toplevel()

    ventana_busqueda.title("🔍 Buscar Producto")
    ventana_busqueda.geometry("950x760")
    ventana_busqueda.config(bg="#1a1a1a")
    ventana_busqueda.resizable(False, False)


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_busqueda,
        text="🔍 BUSCAR PRODUCTOS",
        font=("Arial", 28, "bold"),
        bg="#1a1a1a",
        fg="white"
    )

    titulo.pack(pady=20)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_busqueda,
        text="Busca productos por nombre, letra o categoría",
        font=("Arial", 12),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=3)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_busqueda,
        bg="#333333",
        height=2,
        width=560
    )

    linea.pack(pady=12)


    # ================= FRAME BUSQUEDA ================= #

    frame_busqueda = tk.Frame(
        ventana_busqueda,
        bg="#1a1a1a"
    )

    frame_busqueda.pack(pady=15)


    # ================= ENTRY ================= #

    entrada_busqueda = tk.Entry(
        frame_busqueda,
        font=("Arial", 14),
        width=35,
        bg="#2b2b2b",
        fg="#aaaaaa",
        insertbackground="white",
        relief="flat",
        bd=10
    )

    entrada_busqueda.grid(
        row=0,
        column=0,
        padx=10
    )

    entrada_busqueda.insert(
        0,
        "🔍 Buscar producto..."
    )


    # ================= PLACEHOLDER ================= #

    def borrar_placeholder(event):

        if entrada_busqueda.get() == "🔍 Buscar producto...":

            entrada_busqueda.delete(
                0,
                tk.END
            )

            entrada_busqueda.config(
                fg="white"
            )


    def restaurar_placeholder(event):

        if entrada_busqueda.get() == "":

            entrada_busqueda.insert(
                0,
                "🔍 Buscar producto..."
            )

            entrada_busqueda.config(
                fg="#aaaaaa"
            )


    entrada_busqueda.bind(
        "<FocusIn>",
        borrar_placeholder
    )

    entrada_busqueda.bind(
        "<FocusOut>",
        restaurar_placeholder
    )


    # ================= COMBOBOX ================= #

    categorias = [
        "Todas",
        "Cervezas",
        "Whisky",
        "Vinos",
        "Ron",
        "Vodka",
        "Tequila",
        "Aguardiente"
    ]


    combo_categoria = ttk.Combobox(
        frame_busqueda,
        values=categorias,
        state="readonly",
        width=22,
        font=("Arial", 11)
    )

    combo_categoria.grid(
        row=0,
        column=1,
        padx=10
    )

    combo_categoria.current(0)


    # ================= BOTON BUSCAR ================= #

    btn_buscar = tk.Button(
        frame_busqueda,
        text="🔎 Buscar",
        bg="#FB8C00",
        fg="white",
        activebackground="#FFB74D",
        activeforeground="white",
        font=("Arial", 11, "bold"),
        width=16,
        height=1,
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    btn_buscar.grid(
        row=0,
        column=2,
        padx=10
    )


    # ================= FRAME RESULTADO ================= #

    frame_resultado = tk.Frame(
        ventana_busqueda,
        bg="#1a1a1a"
    )

    frame_resultado.pack(
        pady=10,
        padx=20
    )


    # ================= SCROLL ================= #

    scroll = tk.Scrollbar(
        frame_resultado
    )

    scroll.pack(
        side="right",
        fill="y"
    )


    # ================= AREA TEXTO ================= #

    resultado_texto = tk.Text(
        frame_resultado,
        font=("Consolas", 11),
        bg="#242424",
        fg="white",
        width=100,
        height=22,
        relief="flat",
        bd=10,
        yscrollcommand=scroll.set
    )

    resultado_texto.pack(
        side="left"
    )

    resultado_texto.config(
        state="disabled"
    )

    scroll.config(
        command=resultado_texto.yview
    )


    # ================= FUNCION BUSQUEDA ================= #

    def realizar_busqueda():

        nombre_producto = entrada_busqueda.get()

        categoria = combo_categoria.get()


        if nombre_producto == "🔍 Buscar producto...":

            nombre_producto = ""


        if categoria == "Todas":

            categoria = None


        productos = buscar_producto(
            nombre_producto,
            categoria
        )


        resultado_texto.config(
            state="normal"
        )

        resultado_texto.delete(
            "1.0",
            tk.END
        )


        # ================= RESULTADOS ================= #

        if productos:

            texto = ""


            for producto in productos:

                stock = producto["stock"]


                # ================= ESTADO ================= #

                if stock <= 5:

                    estado = "⚠️ STOCK BAJO"

                elif stock <= 15:

                    estado = "📦 STOCK MEDIO"

                else:

                    estado = "✅ STOCK ALTO"


                texto += (

                    f"📦 CATEGORÍA : {producto['categoria']}\n"
                    f"🍾 CÓDIGO    : {producto['codigo']}\n"
                    f"🥃 PRODUCTO  : {producto['nombre']}\n"
                    f"💰 PRECIO    : ${producto['precio']}\n"
                    f"📦 STOCK     : {producto['stock']}\n"
                    f"📊 ESTADO    : {estado}\n"
                    f"{'═'*70}\n\n"
                )


            resultado_texto.insert(
                tk.END,
                texto
            )

        else:

            resultado_texto.insert(
                tk.END,
                "\n\n⚠️ NO SE ENCONTRARON PRODUCTOS"
            )


        resultado_texto.config(
            state="disabled"
        )


    # ================= ACTIVAR BOTON ================= #

    btn_buscar.config(
        command=realizar_busqueda
    )


    # ================= HOVER ================= #

    def entrar_hover(e):

        btn_buscar.config(
            bg="#FFB74D"
        )


    def salir_hover(e):

        btn_buscar.config(
            bg="#FB8C00"
        )


    btn_buscar.bind(
        "<Enter>",
        entrar_hover
    )

    btn_buscar.bind(
        "<Leave>",
        salir_hover
    )


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_busqueda,
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
        command=ventana_busqueda.destroy
    )

    btn_cerrar.pack(
        pady=12
    )


    # ================= HOVER BOTON CERRAR ================= #

    def hover_cerrar_entrar(e):

        btn_cerrar.config(
            bg="#E53935"
        )


    def hover_cerrar_salir(e):

        btn_cerrar.config(
            bg="#C62828"
        )


    btn_cerrar.bind(
        "<Enter>",
        hover_cerrar_entrar
    )

    btn_cerrar.bind(
        "<Leave>",
        hover_cerrar_salir
    )