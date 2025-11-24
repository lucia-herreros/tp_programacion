from utilidades.utilidades_platos import mostrar_menu_simple, agregar_plato
from validaciones import pedir_precio, pedir_nombre

def modificar_menu():
    print("\n===== MODIFICAR CARTA =====") 

    try:
        # Muestra la carta actual de platos
        mostrar_menu_simple()
    except Exception as e:
        print(f"❌ Error mostrando el menú: {e}")
    
    # Se solicitan al usuario los datos del nuevo plato con validaciones
    print("\n---Datos del nuevo plato---")
    nombre_plato = pedir_nombre()
    precio = pedir_precio()

    # Intenta agregar el plato al archivo JSON
    try:
        resultado = agregar_plato(nombre_plato, precio)

        # Si retorna algo distinto de True, significa que no se pudo agregar
        if resultado is not True:
            print("❌ No se pudo agregar el plato")
            return

        # Mensaje de éxito si todo salió bien
        print("\n✅ Plato agregado con éxito")

    except Exception as e:
        print(f"❌ Error agregando el plato: {e}")
        return False




    