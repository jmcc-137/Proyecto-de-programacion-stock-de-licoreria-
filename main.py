from interfaces.menu_principal import ventana
from logic.funciones_json import cargar_datos
from logic.funciones_inventario import agregar_producto,buscar_producto, registrar_venta

registrar_venta("Budweiser", 15)
producto = buscar_producto("Budweiser")
print(producto)
# agregar_producto(
#     "Cervezas",
#     "C003",
#     "Budweiser",
#     7000,
#     15
# )

# producto = buscar_producto("Budweiser")
# print(producto)

# datos = cargar_datos()
# print(datos)
#ventana.mainloop()