import validaciones
from utilidades import borrar_reservas
import csv
from datetime import datetime, time

def guardar_reserva(r):
    try:
        with open("datos/reservas.csv", "a", newline="") as archivo:
            escritor = csv.writer(archivo)

            # Si el archivo está vacío, se escriben los encabezados
            if archivo.tell() == 0:
                escritor.writerow(["nombre", "personas", "fecha", "hora"])

            # Escribir los datos desde el diccionario 
            escritor.writerow([
                r["nombre"],
                r["personas"],
                r["fecha"],
                r["hora"]
            ])

            print(f"\n✅ Reserva registrada para {r["nombre"]} para {r["personas"]} personas el {r["fecha"]} a las {r["hora"]} hs.")

    except FileNotFoundError:
        print("❌ No se encontró el archivo")
    except KeyError as e:
        print(f"❌ Error con la clave {e}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")


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
    
    try:
        with open("datos/reservas.csv", "r") as archivo:
            # Cada fila se lee como un diccionario
            lector = csv.DictReader(archivo)  
            reservas = list(lector)

            if not reservas:
                print("\n📂 No hay reservas registradas.")
                return

            print("\n--- LISTA DE RESERVAS ---")
            
            for i, r in enumerate(reservas, start=1):
                print(f"{i}. {r['nombre']} - {r['personas']} personas - {r['fecha']} a las {r['hora']}hs")
    
    except FileNotFoundError:
        print("❌ No se encontró el archivo")
    except KeyError as e:
        print(f"❌ Error con la clave {e}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")
