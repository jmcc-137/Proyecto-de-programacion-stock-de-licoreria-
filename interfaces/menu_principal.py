import tkinter as tk

from interfaces.inventario import abrir_inventario
from interfaces.busqueda import abrir_busqueda
from interfaces.faltantes import abrir_faltantes
from interfaces.ventas import abrir_ventas
from interfaces.agregar_producto import abrir_agregar_producto
from interfaces.actualizar_stock import abrir_actualizar_stock
from interfaces.estadisticas import abrir_estadisticas
from interfaces.eliminar_producto import abrir_eliminar_producto


# ================= VENTANA PRINCIPAL ================= #

ventana = tk.Tk()

ventana.title("🍷 Sistema de Licorería")
ventana.geometry("950x900")
ventana.config(bg="#1a1a1a")
ventana.resizable(False, False)


# ================= FUNCION BOTONES ================= #

def crear_boton(frame, texto, color, hover_color, comando):

    boton = tk.Button(
        frame,
        text=texto,
        bg=color,
        fg="white",
        activebackground=hover_color,
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=30,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=comando
    )

    # ================= EFECTO HOVER ================= #

    def on_enter(e):

        boton.config(
            bg=hover_color
        )


    def on_leave(e):

        boton.config(
            bg=color
        )


    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)

    return boton


# ================= TITULO ================= #

titulo = tk.Label(
    ventana,
    text="🍾 SISTEMA DE STOCK 🍾",
    font=("Arial", 28, "bold"),
    bg="#1a1a1a",
    fg="white"
)

titulo.pack(pady=25)


# ================= SUBTITULO ================= #

subtitulo = tk.Label(
    ventana,
    text="Gestión de inventario para licorería",
    font=("Arial", 13),
    bg="#1a1a1a",
    fg="#cfcfcf"
)

subtitulo.pack(pady=5)


# ================= LINEA DECORATIVA ================= #

linea = tk.Frame(
    ventana,
    bg="#333333",
    height=2,
    width=500
)

linea.pack(pady=15)


# ================= FRAME BOTONES ================= #

frame_botones = tk.Frame(
    ventana,
    bg="#1a1a1a"
)

frame_botones.pack(pady=20)


# ================= BOTONES ================= #

# INVENTARIO
btn_inventario = crear_boton(
    frame_botones,
    "📦 Inventario",
    "#1E88E5",
    "#42A5F5",
    abrir_inventario
)

btn_inventario.grid(row=0, column=0, pady=8)


# AGREGAR PRODUCTO
btn_agregar = crear_boton(
    frame_botones,
    "➕ Agregar Producto",
    "#43A047",
    "#66BB6A",
    abrir_agregar_producto
)

btn_agregar.grid(row=1, column=0, pady=8)


# ACTUALIZAR STOCK
btn_stock = crear_boton(
    frame_botones,
    "📦 Actualizar Stock",
    "#00ACC1",
    "#26C6DA",
    abrir_actualizar_stock
)

btn_stock.grid(row=2, column=0, pady=8)


# ELIMINAR PRODUCTO
btn_eliminar = crear_boton(
    frame_botones,
    "🗑️ Eliminar Producto",
    "#E53935",
    "#EF5350",
    abrir_eliminar_producto
)

btn_eliminar.grid(row=3, column=0, pady=8)


# BUSCAR PRODUCTO
btn_busqueda = crear_boton(
    frame_botones,
    "🔍 Buscar Producto",
    "#FB8C00",
    "#FFB74D",
    abrir_busqueda
)

btn_busqueda.grid(row=4, column=0, pady=8)


# REGISTRAR VENTA
btn_ventas = crear_boton(
    frame_botones,
    "💰 Registrar Venta",
    "#8E24AA",
    "#BA68C8",
    abrir_ventas
)

btn_ventas.grid(row=5, column=0, pady=8)


# PRODUCTOS FALTANTES
btn_faltantes = crear_boton(
    frame_botones,
    "⚠️ Productos Faltantes",
    "#F4511E",
    "#FF7043",
    abrir_faltantes
)

btn_faltantes.grid(row=6, column=0, pady=8)


# ESTADISTICAS
btn_estadisticas = crear_boton(
    frame_botones,
    "📊 Estadísticas",
    "#546E7A",
    "#78909C",
    abrir_estadisticas
)

btn_estadisticas.grid(row=7, column=0, pady=8)


# ================= BOTON SALIR ================= #

btn_salir = tk.Button(
    ventana,
    text="❌ Salir",
    bg="#C62828",
    fg="white",
    activebackground="#E53935",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=22,
    height=2,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=ventana.quit
)

btn_salir.pack(pady=15)


# ================= FOOTER ================= #

footer = tk.Label(
    ventana,
    text="🍷 Licorería Python Edition 🍷",
    font=("Arial", 10),
    bg="#1a1a1a",
    fg="#7f7f7f"
)

footer.pack(side="bottom", pady=15)


# ================= MAINLOOP ================= #

ventana.mainloop()