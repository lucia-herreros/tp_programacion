reservas = []  # Lista global temporal

def hacer_reserva():
    print("\n--- HACER UNA RESERVA ---")
    
    # Informar al usuario sobre los horarios del restaurante
    horario_apertura = "19:00 hs"
    horario_cierre = "23:59 hs"
    
    print(f"❗ Por favor, tenga en cuenta que los horarios del restaurante son de {horario_apertura} a {horario_cierre} ❗ \n")

    # Ingreso y validación del nombre de la reserva. 
    # Recorre cada caracter del nombre y comprueba que sea una letra o un espacio y si todo sale bien sale del bucle con el break.
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if len(nombre) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
        elif not all(c.isalpha() or c.isspace() for c in nombre):
            print("❌ El nombre solo puede contener letras y espacios.")
        else:
            break
    
    # Ingreso y validación de la cantidad de personas
    while True:
        try:
            cantidad = int(input("Cantidad de personas: ").strip())
            if cantidad <= 0:
                print("❌ Por favor, ingrese un número mayor a 0.")
            else:
                break
        except ValueError:
            print("❌ Por favor, ingrese solo números.")
    
    # Ingreso y validación de la fecha
    while True:
        fecha = input("Fecha (DD/MM): ").strip()
        try:
            dia, mes = map(int, fecha.split("/"))
            if 1 <= dia <= 31 and 1 <= mes <= 12:
                break
            else: 
                print("❌ Día o mes inválido.")
        except (ValueError, TypeError):
            print("❌ Formato inválido. Ingrese la fecha con el formato DD/MM y utilice solo números (ej: 05/10).") 

    # Ingreso y validación de la fecha
    while True:
        hora = input("Hora (HH:MM): ").strip()
        try:
            h, min = map(int, hora.split(":"))
            if 0 <= h <= 23 and 0 <= min <= 59:
                if h >= 19:
                    break
                else:
                    print("❌ Ingrese un horario válido.")     
            else: 
                print("❌ Ingrese un horario válido.")
        except (ValueError, TypeError):
            print("❌ Formato inválido. Ingrese la hora con el formato HH:MM y utilice solo números (ej: 20:30).") 

    reserva = {
        "nombre": nombre,
        "personas": cantidad,
        "fecha": fecha,
        "hora": hora
    }
    reservas.append(reserva)
    print(f"\n✅ Reserva registrada para {nombre} el {fecha} a las {hora}hs.")

def mostrar_reservas():
    print("\n--- LISTA DE RESERVAS ---")
    if not reservas:
        print("No hay reservas registradas.")
        return
    for i, r in enumerate(reservas, start=1):
        print(f"{i}. {r['nombre']} - {r['personas']} personas - {r['fecha']} {r['hora']}")

