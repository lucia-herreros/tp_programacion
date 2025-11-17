import csv
from datetime import datetime

def borrar_reservas():
    try:
        with open("datos/reservas.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            reservas = list(lector)

        if not reservas:
            return

        hoy = datetime.now().date()
        reservas_actualizadas = []

        for r in reservas:
            try:
                # Convertir la cadena de texto con datetime para comparar con la fecha de hoy
                fecha_reserva = datetime.strptime(r["fecha"], "%d/%m/%Y").date()
                if fecha_reserva >= hoy:
                    reservas_actualizadas.append(r)
            except ValueError:
                # Si alguna fecha está mal formateada se descarta
                continue

        # Sobrescribir el archivo con las reservas vigentes
        with open("datos/reservas.csv", "w", newline="") as archivo:
            campos = ["nombre", "personas", "fecha", "hora"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(reservas_actualizadas)
    
    except FileNotFoundError:
        print("❌ No se encontró el archivo de reservas.")
    except Exception as e:
        print(f"❌ Error al borrar reservas: {e}")
    
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


def leer_reservas():
    try:
        with open("datos/reservas.csv", "r") as archivo:
            # Cada fila se lee como un diccionario
            lector = csv.DictReader(archivo)  
            reservas = list(lector)
            
            return reservas
    
    except FileNotFoundError:
        print("❌ No se encontró el archivo")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")