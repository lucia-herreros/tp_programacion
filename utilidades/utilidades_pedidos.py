def agrupar_pedido(pedido):
    pedido_agrupado = []
    vistos = set() # conjunto para recordar qué platos ya procesamos
    
    for p in pedido:
        # Verificar si ya está en la lista agrupada
        if p["id"] in vistos:
            continue

        cantidad = 0
        for elemento in pedido:
            if elemento["id"] == p["id"]:
                cantidad += 1
        
        vistos.add(p["id"])

        plato = {
            "id": p["id"],
            "nombre": p["nombre"],
            "precio": p["precio"],
            "cantidad": cantidad
        }

        pedido_agrupado.append(plato)
    
    return pedido_agrupado

def mostrar_resumen(nombre, pedido):
    total = 0

    print("\n--- RESUMEN DEL PEDIDO ---")
    print(f"Pedido para: {nombre}")

    for i, item in enumerate(pedido, start=1):
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{i}. {item['nombre']} (x{item['cantidad']}) - ${subtotal}")

    print(f"TOTAL: ${total}")