import validaciones
from utilidades.utilidades_reservas import borrar_reservas, guardar_reserva, leer_reservas
from datetime import datetime, time

def hacer_reserva():
    print("\n--- HACER UNA RESERVA ---")
    
    # Informar al usuario sobre los horarios del restaurante
    apertura = time(19, 0)
    cierre = time(22, 0)
    
    print(f"📅 Horario disponible para reservas: desde las {apertura.strftime("%H:%M hs")} hasta las {cierre.strftime("%H:%M hs")}")
    
    # Ingreso y validación del nombre  
    nombre = validaciones.pedir_nombre()
    
    # Ingreso y validación de la cantidad de personas
    cantidad = validaciones.pedir_cantidad_personas()
    
    # Ingreso y validación de la fecha
    fecha = validaciones.pedir_fecha()

    # Ingreso y validación de la hora
    hora = validaciones.pedir_hora(apertura, cierre)

    reserva = {
        "nombre": nombre,
        "personas": cantidad,
        "fecha": fecha,
        "hora": hora
    }

    guardar_reserva(reserva)
    

def mostrar_reservas():
    # Borra todas las reservas anteriores a la fecha de hoy
    borrar_reservas()

    reservas = leer_reservas()

    if not reservas:
        print("\n📂 No hay reservas registradas.")
    else:
        print("\n--- LISTA DE RESERVAS ---")
            
        for i, r in enumerate(reservas, start=1):
            print(f"{i}. {r['nombre']} - {r['personas']} personas - {r['fecha']} a las {r['hora']}hs")
    

