# TP Restaurante — Proyecto en Python 🍽️

## Descripción

Este proyecto es un sistema de gestión para un restaurante, implementado íntegramente en **Python**.  
Permite manejar los elementos esenciales de un restaurante: el menú de platos, los pedidos, las reservas y la manipulación de datos de platos almacenados en archivo JSON.

---

## Tecnologías / herramientas utilizadas

- Python 3.x  
- Módulos estándar de Python (json, datetime, entre otros.)  
- Archivo `platos.json` para persistir datos de platos  
- (Toda la persistencia de platos está en JSON)  
- Estructura modular con archivos para cada dominio funcional: menú, pedidos, reservas, etc.

---

## Estructura del proyecto

```text
tp_programacion/
│
├── main.py            # Punto de entrada del programa
├── menu.py            # Lógica relacionada al menú de platos
├── pedidos.py         # Gestión de pedidos (alta, seguimiento, cierre)
├── reservas.py        # Gestión de reservas de mesas
├── platos.json         # Datos persistentes de los platos del menú
└── README.md           # Este archivo
