from datetime import datetime, time

def pedir_opcion():
    while True:
        try: 
            opcion = int(input(">").strip())
            return opcion
        except ValueError:
            print("⚠️ Por favor ingrese un número.\n")
        

def pedir_nombre():
    nombre = input("\nIngrese un nombre: ").strip()
    if len(nombre) < 3 or not all(c.isalpha() or c.isspace() for c in nombre):
        print("❌ Nombre inválido. Intente de nuevo.")
        return pedir_nombre()  # La función vuelve a llamarse a sí misma
    return nombre.title() # Normalizar

def pedir_cantidad_personas():
    while True:
        try:
            cantidad = int(input("Cantidad de personas: ").strip())
            if cantidad <= 0:
                print("❌ Por favor, ingrese un número mayor a 0.")
            elif cantidad > 10:
                print("❌ No se pueden realizar reservas para más de 10 personas.")
            else:
                return cantidad
        except ValueError:
            print("❌ Por favor, ingrese solo números enteros.")

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

def pedir_precio():
    while True:
        try:
            precio = int(input("Ingrese el precio del plato: ").strip())
            if precio <= 0:
                print("❌ El precio debe ser mayor a 0.")
            else:
                return precio
        except ValueError:
            print("❌ Ingrese un número válido para el precio.")