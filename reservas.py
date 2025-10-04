reservas = []  # Lista global temporal

def hacer_reserva():
    print("\n--- HACER UNA RESERVA ---")
    nombre = input("Ingrese su nombre: ").strip()
    cantidad = input("Cantidad de personas: ").strip()
    fecha = input("Fecha (DD/MM): ").strip()
    hora = input("Hora (HH:MM): ").strip()

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
