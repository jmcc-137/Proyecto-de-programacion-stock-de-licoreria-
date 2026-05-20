import tkinter as tk


def abrir_ventas():

    ventana_ventas = tk.Toplevel()

    ventana_ventas.title("💰 Registrar Venta")
    ventana_ventas.geometry("800x600")
    ventana_ventas.config(bg="#1e1e1e")


    titulo = tk.Label(
        ventana_ventas,
        text="💰 REGISTRAR VENTA",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="white"
    )

    titulo.pack(pady=20)


    label_producto = tk.Label(
        ventana_ventas,
        text="Nombre del producto",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12)
    )

    label_producto.pack(pady=10)


    entrada_producto = tk.Entry(
        ventana_ventas,
        font=("Arial", 12),
        width=30
    )

    entrada_producto.pack(pady=5)


    label_cantidad = tk.Label(
        ventana_ventas,
        text="Cantidad",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12)
    )

    label_cantidad.pack(pady=10)


    entrada_cantidad = tk.Entry(
        ventana_ventas,
        font=("Arial", 12),
        width=30
    )

    entrada_cantidad.pack(pady=5)


    btn_vender = tk.Button(
        ventana_ventas,
        text="💸 Registrar Venta",
        bg="#9C27B0",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        relief="flat"
    )

    btn_vender.pack(pady=20)