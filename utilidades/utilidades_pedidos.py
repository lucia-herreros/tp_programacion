def agrupar_pedido(pedido):
    # Lista donde se guardarán los platos agrupados con su cantidad
    pedido_agrupado = []
    # Conjunto para recordar qué IDs de platos ya se procesaron
    vistos = set() 
    
    # Recorrer todos los platos del pedido original
    for p in pedido:
        # Verificar si ya está en la lista agrupada
        if p["id"] in vistos:
            continue
        
        # Contar cuántas veces aparece el mismo plato en el pedido
        cantidad = 0
        for elemento in pedido:
            if elemento["id"] == p["id"]:
                cantidad += 1
        
        # Registra que ya se procesó este plato
        vistos.add(p["id"])

        # Crear un diccionario con los datos del plato y su cantidad total
        plato = {
            "id": p["id"],
            "nombre": p["nombre"],
            "precio": p["precio"],
            "cantidad": cantidad
        }
        
        # Guardarlo en la lista agrupada        
        pedido_agrupado.append(plato)
    
    # Devolver la lista de platos sin repeticiones
    return pedido_agrupado

def mostrar_resumen(nombre, pedido):
    # Variable para acumular el total del pedido
    total = 0

    print("\n--- RESUMEN DEL PEDIDO ---")
    print(f"Pedido para: {nombre}")

    # Mostrar cada plato con su cantidad y subtotal
    for i, item in enumerate(pedido, start=1):
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{i}. {item['nombre']} (x{item['cantidad']}) - ${subtotal}")

    # Mostrar el total a pagar
    print(f"TOTAL: ${total}")