import json

def hacer_pedido():
    print("\n--- HACER UN PEDIDO ---")

    try:
        with open("datos/platos.json", "r") as archivo:
            platos = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de platos.")
        return
    except json.JSONDecodeError:
        print("Error al leer el archivo de platos.")
        return

    # Mostrar menú simple
    for p in platos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']}")

    pedido = []
    total = 0

    # Ingreso y validación del nombre para el pedido
    # Recorre cada caracter del nombre y comprueba que sea una letra o un espacio y si todo sale bien sale del bucle con el break.
    while True:
        nombre = input("\nIngrese su nombre: ").strip()
        if len(nombre) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
        elif not all(c.isalpha() or c.isspace() for c in nombre):
            print("❌ El nombre solo puede contener letras y espacios.")
        else:
            break
    
    # Ingreso y validación de platos del pedido
    while True:
        opcion = input("\nIngrese el ID del plato (o 'fin' para terminar): ").strip().lower()
        if opcion == "fin":
            break

        if not opcion.isdigit():
            print("❌ Por favor ingrese un número válido.")
            continue

        opcion = int(opcion)
        plato = next((p for p in platos if p["id"] == opcion), None)

        if plato:
            pedido.append(plato)
            total += plato["precio"]
            print(f"✅ {plato['nombre']} agregado al pedido.")
        else:
            print("❌ ID inválido, intente nuevamente.")
            
    # Verifica si la lista "pedido" tiene algun plato agregado, si hay platos muestra un resumen del pedido listando su nombre y su precio
    # Junto con su total. Si la lista esta vacia muestra un mensaje indicando que no se agrego ningun plato al pedido.
    if pedido:
        print("\n--- RESUMEN DEL PEDIDO ---")
        print(f"Pedido para {nombre}")
        for p in pedido:
            print(f"- {p['nombre']} (${p['precio']})")
        print(f"TOTAL: ${total}")
    else:
        print("No se agregó ningún plato al pedido.")

