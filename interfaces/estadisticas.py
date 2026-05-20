import tkinter as tk

from logic.funciones_inventario import (
    total_productos,
    total_stock,
    valor_total_inventario,
    producto_mayor_stock
)


def abrir_estadisticas():

    ventana_estadisticas = tk.Toplevel()

    ventana_estadisticas.title("📊 Estadísticas")
    ventana_estadisticas.geometry("700x600")
    ventana_estadisticas.config(bg="#1e1e1e")
    ventana_estadisticas.resizable(False, False)


    # ================= TITULO ================= #

    titulo = tk.Label(
        ventana_estadisticas,
        text="📊 ESTADÍSTICAS",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="white"
    )

    titulo.pack(pady=20)


    # ================= DATOS ================= #

    producto_top = producto_mayor_stock()


    estadisticas = [
        f"🍾 Total de productos: {total_productos()}",
        f"📦 Total de unidades: {total_stock()}",
        f"💰 Valor total inventario: ${valor_total_inventario()}",
        f"🏆 Producto con más stock: {producto_top['nombre']}",
        f"📈 Stock más alto: {producto_top['stock']}"
    ]


    frame = tk.Frame(
        ventana_estadisticas,
        bg="#1e1e1e"
    )

    frame.pack(pady=40)


    for texto in estadisticas:

        label = tk.Label(
            frame,
            text=texto,
            font=("Arial", 14, "bold"),
            bg="#2b2b2b",
            fg="white",
            width=40,
            height=2
        )

        label.pack(pady=10)


    # ================= BOTON CERRAR ================= #

    btn_cerrar = tk.Button(
        ventana_estadisticas,
        text="❌ Cerrar",
        bg="#d32f2f",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        relief="flat",
        cursor="hand2",
        command=ventana_estadisticas.destroy
    )

    btn_cerrar.pack(pady=20)