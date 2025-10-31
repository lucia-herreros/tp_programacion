from datetime import datetime, time

def pedir_nombre():
    nombre = input("\nIngrese su nombre: ").strip()
    if len(nombre) < 3 or not all(c.isalpha() or c.isspace() for c in nombre):
        print("❌ Nombre inválido. Intente de nuevo.")
        return pedir_nombre()  # La función vuelve a llamarse a sí misma
    return nombre

def pedir_cantidad_personas():
    while True:
        try:
            cantidad = int(input("Cantidad de personas: ").strip())
            if cantidad <= 0:
                print("❌ Por favor, ingrese un número mayor a 0.")
            else:
                return cantidad
        except ValueError:
            print("❌ Por favor, ingrese solo números.")

def pedir_fecha():
    while True:
        try:
            fecha_ingresada = input("Fecha (DD/MM): ").strip()
            fecha = datetime.strptime(fecha_ingresada + f"/{datetime.now().year}", "%d/%m/%Y").date()
            
            hoy = datetime.now().date()
            if fecha >= hoy:
                fecha = fecha.strftime("%d/%m/%Y") # convertir a texto
                return fecha
            print("❌ No puede reservar para fechas pasadas.")
        except ValueError:
            print("❌ Formato inválido. Use DD/MM (ej: 05/11).")

def pedir_hora(apertura, cierre):
    while True:
        try:
            hora_ingresada = input("Hora (HH:MM): ").strip()
            hora = datetime.strptime(hora_ingresada, "%H:%M").time()
            if apertura <= hora <= cierre:
                hora = hora.strftime("%H:%M")  # convertir a texto
                return hora
            print(f"❌ Solo se aceptan reservas entre {apertura.strftime('%H:%M')} y {cierre.strftime('%H:%M')}.")
        except ValueError:
            print("❌ Formato inválido. Use HH:MM (ej: 20:30).")