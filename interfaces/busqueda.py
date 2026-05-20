import tkinter as tk
from tkinter import messagebox

from logic.funciones_inventario import buscar_producto


def abrir_busqueda():

    ventana_busqueda = tk.Toplevel()

    ventana_busqueda.title("🔍 Buscar Producto")
    ventana_busqueda.geometry("900x720")
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

    titulo.pack(pady=25)


    # ================= SUBTITULO ================= #

    subtitulo = tk.Label(
        ventana_busqueda,
        text="Busca productos por nombre o letra",
        font=("Arial", 13),
        bg="#1a1a1a",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=5)


    # ================= LINEA ================= #

    linea = tk.Frame(
        ventana_busqueda,
        bg="#333333",
        height=2,
        width=500
    )

    linea.pack(pady=15)


    # ================= FRAME BUSQUEDA ================= #

    frame_busqueda = tk.Frame(
        ventana_busqueda,
        bg="#1a1a1a"
    )

    frame_busqueda.pack(pady=20)


    # ================= PLACEHOLDER ================= #

    entrada_busqueda = tk.Entry(
        frame_busqueda,
        font=("Arial", 14),
        width=40,
        bg="#2b2b2b",
        fg="#aaaaaa",
        insertbackground="white",
        relief="flat",
        bd=10
    )

    entrada_busqueda.insert(
        0,
        "🔍 Buscar producto..."
    )

    entrada_busqueda.pack()


    # ================= FUNCION PLACEHOLDER ================= #

    def borrar_placeholder(event):

        if entrada_busqueda.get() == "🔍 Buscar producto...":

            entrada_busqueda.delete(0, tk.END)

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


    # ================= FRAME RESULTADOS ================= #

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
        frame_resultado,
        bg="#2b2b2b",
        troughcolor="#1a1a1a",
        activebackground="#444444"
    )

    scroll.pack(
        side="right",
        fill="y"
    )


    # ================= AREA RESULTADOS ================= #

    resultado_texto = tk.Text(
        frame_resultado,
        font=("Consolas", 12),
        bg="#242424",
        fg="white",
        width=80,
        height=15,
        relief="flat",
        bd=10,
        yscrollcommand=scroll.set
    )

    resultado_texto.pack(side="left")

    resultado_texto.config(state="disabled")

    scroll.config(command=resultado_texto.yview)


    # ================= FUNCION BUSCAR ================= #

    def realizar_busqueda():

        nombre_producto = entrada_busqueda.get()


        if (
            nombre_producto == "" or
            nombre_producto == "🔍 Buscar producto..."
        ):

            messagebox.showwarning(
                "Advertencia",
                "⚠️ Ingresa un producto para buscar"
            )

            return


        productos = buscar_producto(nombre_producto)


        resultado_texto.config(state="normal")

        resultado_texto.delete("1.0", tk.END)


        if productos:

            texto = ""


            for producto in productos:

                texto += (
                    f"🍾 CÓDIGO : {producto['codigo']}\n"
                    f"🥃 PRODUCTO: {producto['nombre']}\n"
                    f"💰 PRECIO  : ${producto['precio']}\n"
                    f"📦 STOCK   : {producto['stock']}\n"
                    f"{'═'*55}\n\n"
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


        resultado_texto.config(state="disabled")


    # ================= BOTON BUSCAR ================= #

    btn_buscar = tk.Button(
        ventana_busqueda,
        text="🔎 Buscar",
        bg="#FB8C00",
        fg="white",
        activebackground="#FFB74D",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=22,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=realizar_busqueda
    )

    btn_buscar.pack(pady=15)


    # ================= EFECTO HOVER ================= #

    def hover_entrar(e):

        btn_buscar.config(
            bg="#FFB74D"
        )


    def hover_salir(e):

        btn_buscar.config(
            bg="#FB8C00"
        )


    btn_buscar.bind(
        "<Enter>",
        hover_entrar
    )

    btn_buscar.bind(
        "<Leave>",
        hover_salir
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

    btn_cerrar.pack(pady=15)