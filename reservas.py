import validaciones
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
    horario_apertura = time(19, 0)
    horario_cierre = time(22, 0)
    
    print(f"❗ Por favor, tenga en cuenta que solo se toman reservas desde las {horario_apertura.strftime("%H:%M hs")} hasta las {horario_cierre.strftime("%H:%M hs")}")
    
    # Ingreso y validación del nombre  
    nombre = validaciones.pedir_nombre()
    
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
        input_fecha = input("Fecha (DD/MM): ").strip()
        try:
            # Validar formato y valores correctos de día y mes
            fecha = datetime.strptime(input_fecha + f"/{datetime.now().year}", "%d/%m/%Y").date()
            hoy = datetime.now().date()

            # Verificar que la fecha ingresada sea igual o posterior a la fecha actual 
            if fecha < hoy:
                print("❌ No se pueden realizar reservas para fechas anteriores a hoy.")
            else:
                break
        except (ValueError, TypeError):
            print("❌ Formato o valor inválido. Ingrese la fecha con el formato DD/MM y utilice solo números (ej: 05/10).") 

    # Ingreso y validación de la hora
    while True:
        input_hora = input("Hora (HH:MM): ").strip()
        try:
            hora = datetime.strptime(input_hora, "%H:%M").time()

            if horario_apertura <= hora <= horario_cierre:
                break
            else:
                print(f"❌ El restaurante solo acepta reservas entre {horario_apertura.strftime("%H:%M hs")} y {horario_cierre.strftime("%H:%M hs")}.")
            
        except (ValueError, TypeError):
            print("❌ Formato inválido. Ingrese la hora con el formato HH:MM y utilice solo números (ej: 20:30).") 

    reserva = {
        "nombre": nombre,
        "personas": cantidad,
        "fecha": fecha,
        "hora": hora
    }

    guardar_reserva(reserva)
    

def mostrar_reservas():    
    try:
        with open("datos/reservas.csv", "r") as archivo:
            # Cada fila se lee como un diccionario
            lector = csv.DictReader(archivo)  
            reservas = list(lector)

            if not reservas:
                print("\nNo hay reservas registradas.")
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
