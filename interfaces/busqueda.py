import tkinter as tk


def abrir_busqueda():

    ventana_busqueda = tk.Toplevel()

    ventana_busqueda.title("🔍 Buscar Producto")
    ventana_busqueda.geometry("800x500")
    ventana_busqueda.config(bg="#1e1e1e")


    titulo = tk.Label(
        ventana_busqueda,
        text="🔍 BUSCAR PRODUCTO",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="white"
    )

    titulo.pack(pady=20)


    entrada = tk.Entry(
        ventana_busqueda,
        font=("Arial", 14),
        width=30
    )

    entrada.pack(pady=20)


    btn_buscar = tk.Button(
        ventana_busqueda,
        text="Buscar",
        bg="#FF9800",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        relief="flat"
    )

    btn_buscar.pack(pady=10)