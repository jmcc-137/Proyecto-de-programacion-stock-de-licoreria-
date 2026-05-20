import tkinter as tk


def abrir_faltantes():

    ventana_faltantes = tk.Toplevel()

    ventana_faltantes.title("⚠️ Productos Faltantes")
    ventana_faltantes.geometry("800x500")
    ventana_faltantes.config(bg="#1e1e1e")


    titulo = tk.Label(
        ventana_faltantes,
        text="⚠️ PRODUCTOS FALTANTES",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="white"
    )

    titulo.pack(pady=20)


    lista = tk.Listbox(
        ventana_faltantes,
        width=50,
        height=15,
        font=("Arial", 12)
    )

    lista.pack(pady=20)


    # EJEMPLOS

    lista.insert(tk.END, "Old Parr")
    lista.insert(tk.END, "Corona Extra")
    lista.insert(tk.END, "Jack Daniels")