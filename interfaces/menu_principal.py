import tkinter as tk
from interfaces.inventario import abrir_inventario
from interfaces.busqueda import abrir_busqueda
from interfaces.faltantes import abrir_faltantes
from interfaces.ventas import abrir_ventas



ventana = tk.Tk()

ventana.title("🍷 Sistema de Licorería")
ventana.geometry("900x750")
ventana.config(bg="#1e1e1e")
ventana.resizable(False, False)



def crear_boton(frame, texto, color, comando):

    boton = tk.Button(
        frame,
        text=texto,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="flat",
        cursor="hand2",
        command=comando
    )

    return boton

titulo = tk.Label(
    ventana,
    text="🍾 SISTEMA DE STOCK 🍾",
    font=("Arial", 26, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=20)


subtitulo = tk.Label(
    ventana,
    text="Gestión de inventario para licorería",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#cfcfcf"
)

subtitulo.pack(pady=5)

frame_botones = tk.Frame(
    ventana,
    bg="#1e1e1e"
)

frame_botones.pack(pady=20)



btn_inventario = crear_boton(
    frame_botones,
    "📦 Inventario",
    "#2196F3",
    abrir_inventario
)

btn_inventario.grid(row=0, column=0, pady=10)


btn_agregar = crear_boton(
    frame_botones,
    "➕ Agregar Producto",
    "#4CAF50",
    lambda: print("Agregar producto")
)

btn_agregar.grid(row=1, column=0, pady=10)


btn_busqueda = crear_boton(
    frame_botones,
    "🔍 Buscar Producto",
    "#FF9800",
    abrir_busqueda
)

btn_busqueda.grid(row=2, column=0, pady=10)


btn_faltantes = crear_boton(
    frame_botones,
    "⚠️ Productos Faltantes",
    "#f44336",
    abrir_faltantes
)

btn_faltantes.grid(row=3, column=0, pady=10)


btn_ventas = crear_boton(
    frame_botones,
    "💰 Registrar Venta",
    "#9C27B0",
    abrir_ventas
)

btn_ventas.grid(row=4, column=0, pady=10)


btn_estadisticas = crear_boton(
    frame_botones,
    "📊 Estadísticas",
    "#607D8B",
    lambda: print("Estadísticas")
)

btn_estadisticas.grid(row=5, column=0, pady=10)



btn_salir = tk.Button(
    ventana,
    text="❌ Salir",
    bg="#d32f2f",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    relief="flat",
    cursor="hand2",
    command=ventana.quit
)

btn_salir.pack(pady=20)

footer = tk.Label(
    ventana,
    text="🍷 Licorería Python Edition 🍷",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="#8f8f8f"
)

footer.pack(side="bottom", pady=10)
ventana.mainloop()
