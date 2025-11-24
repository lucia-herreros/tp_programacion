# TP Restaurante Express 🍽️

## Descripción

Este proyecto es un sistema de gestión para un restaurante, implementado íntegramente en **Python**. 

Permite manejar los elementos esenciales de un restaurante, facilitando la administración de platos, pedidos y reservas de manera eficiente.

## Funcionalidades Principales

* **Gestión de Menú:** Alta, baja y modificación de platos.
* **Gestión de Pedidos:** Creación, seguimiento y cierre de pedidos de clientes.
* **Reservas:** Administración de reservas de mesas.
* **Validaciones:** Control robusto de errores en la entrada de datos del usuario.
* **Persistencia de Datos:** Almacenamiento de información en archivos JSON.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías Estándar:** `json`, `datetime`, `os`, etc.
* **Almacenamiento:** Archivos JSON para persistencia de datos.

## Estructura del Proyecto

```text
tp_programacion/
│
├── datos/              # Archivos de persistencia (platos.json)
├── utilidades/         # Funciones auxiliares y herramientas comunes
├── main.py             # Punto de entrada principal del programa
├── menu.py             # Lógica de interacción y visualización del menú
├── platos.py           # Lógica específica para la entidad "Plato"
├── pedidos.py          # Lógica para la gestión de pedidos
├── reservas.py         # Lógica para la gestión de reservas
└── validaciones.py     # Módulo de validación de entradas
