import validaciones
from utilidades.utilidades_pedidos import agrupar_pedido, mostrar_resumen
from utilidades.utilidades_platos import cargar_platos, mostrar_menu_simple              

def modificar_pedido(nombre, pedido):
    # Si el pedido está vacío, no hay nada para modificar
    if not pedido:
        print("\nNo hay platos para modificar.")
        return 
    
    # Bucle para permitir modificar varias veces hasta que el usuario salga
    while True:
        # Agrupa los platos iguales para mostrar cantidades
        agrupado = agrupar_pedido(pedido)

        # Muestra el resumen del pedido actual
        mostrar_resumen(nombre, agrupado)

        print("\nIngrese el número del plato para eliminar UNA unidad (0 para volver): ")
        opcion = validaciones.pedir_opcion()

        if opcion == 0:
            return
        elif opcion < 0 or opcion > len(agrupado):
            print("❌ Número fuera de rango.")
            continue
        
        # Obtener el plato seleccionado
        seleccionado = agrupado[opcion - 1]
        id_plato = seleccionado["id"]
        
        eliminado = False
        
        # Buscar en la lista original y eliminar una unidad
        for i, elemento in enumerate(pedido):
            if elemento["id"] == id_plato:
                del pedido[i]
                eliminado = True
                break
        
        # Resultado de la eliminación
        if eliminado:
            print(f"🗑 Se eliminó una unidad de '{seleccionado['nombre']}'.")
        else:
            print("❌ No se encontró la unidad a eliminar.")

        # Si ya no quedan platos, salir
        if not pedido:
            print("\nEl pedido quedó vacío.")
            return

def gestionar_pedido(nombre, pedido):
    """
    Menú para confirmar, modificar o descartar el pedido.
    """
    # Menú con opciones para el pedido
    while True:
        # Mostrar resumen del pedido actual
        agrupado = agrupar_pedido(pedido)
        mostrar_resumen(nombre, agrupado)

        print("\nElija una opción:")
        print("1. Confirmar pedido")  
        print("2. Modificar pedido")
        print("3. Descartar pedido")

        opcion = validaciones.pedir_opcion()

        # Confirmar el pedido
        if opcion == 1:
            print("\n✅ Pedido confirmado. ¡Gracias!")
            return True
        
        # Modificar el pedido (eliminar elementos)
        elif opcion == 2:
            modificar_pedido(nombre, pedido)
            
            # Si el pedido quedó vacío tras la modificación
            if not pedido:
                print("\n❌ No quedan platos en el pedido.")
                return False
        
        # Descartar el pedido completo
        elif opcion == 3:
            print("🗑 Se descartó el pedido")
            return False
        else:
            print("❌ Opción inválida.\n")


def hacer_pedido():
    print("\n--- HACER UN PEDIDO ---")

    # Cargar la lista completa de platos disponibles
    platos = cargar_platos()

    # Si no hay platos disponibles, se termina 
    if not platos: 
        print("❌ No hay platos disponibles en la carta.") 
        return
    
    mostrar_menu_simple()

    pedido = []

    # Ingreso y validación del nombre para el pedido
    nombre = validaciones.pedir_nombre()
    

    # Ingreso y validación de platos del pedido
    while True:
        print("\nIngrese el ID del plato (0 para terminar): ")
        opcion = validaciones.pedir_opcion()
        
        if opcion == 0:
            break
        
        # Buscar el plato seleccionado por ID
        plato = next((p for p in platos if p["id"] == opcion), None)

        # Si existe, agregarlo al pedido
        if plato:
            pedido.append(plato)
            print(f"✅ {plato['nombre']} agregado al pedido.")
        else:
            print("❌ ID inválido, intente nuevamente.")

    # Si el usuario no eligió nada, se cancela el pedido             
    if not pedido:
        print("No se agregó ningún plato al pedido.")
        return
    
    # Gestionar pedido
    gestionar_pedido(nombre, pedido)

    
