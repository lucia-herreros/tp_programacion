import validaciones
from utilidades.utilidades_pedidos import agrupar_pedido, mostrar_resumen
from utilidades.utilidades_platos import cargar_platos              

def modificar_pedido(nombre, pedido):
    if not pedido:
        print("\nNo hay platos para modificar.")
        return 
    
    while True:
        agrupado = agrupar_pedido(pedido)
        mostrar_resumen(nombre, agrupado)

        print("\nIngrese el número del plato para eliminar UNA unidad (0 para volver): ")
        opcion = validaciones.pedir_opcion()

        if opcion == 0:
            return
        elif opcion < 0 or opcion > len(agrupado):
            print("❌ Número fuera de rango.")
            continue

        seleccionado = agrupado[opcion - 1]
        id_plato = seleccionado["id"]
        
        eliminado = False
        
        for i, elemento in enumerate(pedido):
            if elemento["id"] == id_plato:
                del pedido[i]
                eliminado = True
                break

        if eliminado:
            print(f"🗑 Se eliminó una unidad de '{seleccionado['nombre']}'.")
        else:
            print("❌ No se encontró la unidad a eliminar.")

        if not pedido:
            print("\nEl pedido quedó vacío.")
            return

def hacer_pedido():
    print("\n--- HACER UN PEDIDO ---")

    platos = cargar_platos()

    # Mostrar menú simple
    for p in platos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']}")

    pedido = []

    # Ingreso y validación del nombre para el pedido
    nombre = validaciones.pedir_nombre()
    
    # Ingreso y validación de platos del pedido
    while True:
        print("\nIngrese el ID del plato (0 para terminar): ")
        opcion = validaciones.pedir_opcion()
        
        if opcion == 0:
            break

        plato = next((p for p in platos if p["id"] == opcion), None)

        if plato:
            pedido.append(plato)
            print(f"✅ {plato['nombre']} agregado al pedido.")
        else:
            print("❌ ID inválido, intente nuevamente.")
              
    if not pedido:
        print("No se agregó ningún plato al pedido.")
        return

    while True:
        agrupado = agrupar_pedido(pedido)
        mostrar_resumen(nombre, agrupado)

        print("\nElija una opción:")
        print("1. Confirmar pedido")  
        print("2. Modificar pedido")
        print("3. Descartar pedido")

        opcion = validaciones.pedir_opcion()

        if opcion == 1:
            print("\n✅ Pedido confirmado. ¡Gracias!")
            return
        elif opcion == 2:
            modificar_pedido(nombre, pedido)
            if not pedido:
                print("\n❌ No quedan platos en el pedido.")
                return
        elif opcion == 3:
            print("🗑 Se descartó el pedido")
            return
        else:
            print("❌ Opción inválida.\n")
