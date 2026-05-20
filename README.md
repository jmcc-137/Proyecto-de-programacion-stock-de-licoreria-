# 🍷 Sistema de Gestión de Stock para Licorería

Aplicación de escritorio desarrollada en **Python** utilizando **Tkinter** para la gestión de inventario de una licorería.

El sistema permite administrar productos, controlar el stock, registrar ventas y visualizar productos agotados mediante una interfaz gráfica moderna y organizada.

---

# 📌 Características

✅ Gestión completa de inventario  
✅ Registro de productos  
✅ Actualización de stock  
✅ Registro de ventas  
✅ Búsqueda de productos  
✅ Control de productos agotados  
✅ Eliminación de productos  
✅ Persistencia de datos usando JSON  
✅ Interfaz gráfica con Tkinter  
✅ Diseño modular del proyecto  

---

# 🖥️ Tecnologías Utilizadas

- Python 3
- Tkinter
- JSON
- Git & GitHub
- Visual Studio Code

---

# 📂 Estructura del Proyecto

```bash
Sistema_Gestion_Stock_Licoreria/
│
├── data/
│   └── licoreria.json
│
├── interfaces/
│   ├── menu_principal.py
│   ├── inventario.py
│   ├── agregar_producto.py
│   ├── actualizar_stock.py
│   ├── ventas.py
│   ├── busqueda.py
│   ├── faltantes.py
│   ├── eliminar_producto.py
│   └── estadisticas.py
│
├── logic/
│   ├── funciones_json.py
│   └── funciones_inventario.py
│
├── main.py
└── README.md
```

---

# ⚙️ Funcionalidades del Sistema

## 📦 Inventario

Visualiza todos los productos registrados dentro del sistema mediante una tabla organizada.

---

## ➕ Agregar Producto

Permite registrar nuevos productos indicando:

- Categoría
- Código
- Nombre
- Precio
- Stock

---

## 📦 Actualizar Stock

Permite agregar nuevas unidades a productos ya existentes.

---

## 🔍 Buscar Producto

Permite buscar bebidas por:

- Nombre completo
- Letras
- Coincidencias parciales

---

## 💰 Registrar Venta

Permite registrar ventas y disminuir automáticamente el stock del producto seleccionado.

---

## ⚠️ Productos Faltantes

Muestra automáticamente los productos agotados o sin stock disponible.

---

## ❌ Eliminar Producto

Permite eliminar productos del inventario.

---

# 💾 Persistencia de Datos

La información se almacena utilizando archivos JSON.

Esto permite:

- Guardar datos permanentemente
- Recuperar productos al iniciar el sistema
- Simular una pequeña base de datos

---

# 🚀 Cómo Ejecutar el Proyecto

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

---

## 2️⃣ Entrar al proyecto

```bash
cd Sistema_Gestion_Stock_Licoreria
```

---

## 3️⃣ Ejecutar el programa

```bash
python main.py
```

---

# 📚 Conceptos de Programación Aplicados

- Variables
- Condicionales
- Ciclos
- Funciones
- Listas
- Diccionarios
- Manejo de archivos
- Modularización
- Interfaces gráficas

---

# 👨‍💻 Autor(es)

- Tu Nombre
- Nombre compañero

---

# 🎓 Proyecto Académico

Proyecto desarrollado para la asignatura:

**Fundamentos de Programación**  
Universidad Autónoma de Bucaramanga

---

# 📄 Licencia

Proyecto de uso académico y educativo.