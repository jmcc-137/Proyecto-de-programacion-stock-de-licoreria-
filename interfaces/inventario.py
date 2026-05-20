import tkinter as tk


def abrir_inventario():

    ventana_inventario = tk.Toplevel()

    ventana_inventario.title("📦 Inventario")
    ventana_inventario.geometry("900x700")
    ventana_inventario.config(bg="#1e1e1e")



    titulo = tk.Label(
        ventana_inventario,
        text="📦 INVENTARIO DE LICORES",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="white"
    )

    titulo.pack(pady=20)



    subtitulo = tk.Label(
        ventana_inventario,
        text="Seleccione una categoría",
        font=("Arial", 12),
        bg="#1e1e1e",
        fg="#cfcfcf"
    )

    subtitulo.pack(pady=5)



    frame = tk.Frame(
        ventana_inventario,
        bg="#1e1e1e"
    )

    frame.pack(pady=30)



    def crear_boton(texto, color):

        boton = tk.Button(
            frame,
            text=texto,
            bg=color,
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            relief="flat",
            cursor="hand2"
        )

        return boton



    categorias = [
        ("🍺 Cervezas", "#fbc02d"),
        ("🥃 Whisky", "#6d4c41"),
        ("🍷 Vinos", "#c2185b"),
        ("🍹 Ron", "#00897b"),
        ("🍾 Vodka", "#5e35b1"),
        ("🍸 Tequila", "#fb8c00")
    ]


    fila = 0

    for texto, color in categorias:

        boton = crear_boton(texto, color)

        boton.grid(
            row=fila,
            column=0,
            pady=8
        )

        fila += 1


    btn_cerrar = tk.Button(
        ventana_inventario,
        text="❌ Cerrar",
        bg="#d32f2f",
        fg="white",
        font=("Arial", 11, "bold"),
        width=20,
        height=2,
        relief="flat",
        command=ventana_inventario.destroy
    )

    btn_cerrar.pack(pady=20)