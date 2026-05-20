import json

RUTA_ARCHIVO = "inventario.json"


def cargar_datos():
    try:
        with open(RUTA_ARCHIVO,"r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return {}
    
def guardar_datos(datos):
    
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )
