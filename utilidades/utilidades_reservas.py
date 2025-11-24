import csv
from datetime import datetime

RUTA_RESERVAS = "datos/reservas.csv"

def borrar_reservas():
    """
    Elimina del archivo CSV todas las reservas cuyas fechas ya pasaron.
    Solo deja las reservas con fecha igual o posterior al día actual.
    """
    try:
        # Abrir el archivo y leer todas las reservas como diccionarios
        with open(RUTA_RESERVAS, "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            reservas = list(lector)

        # Si no hay reservas, termina
        if not reservas:
            return

        hoy = datetime.now().date()
        reservas_actualizadas = []

        # Recorrer cada reserva registrada
        for r in reservas:
            try:
                # Convertir la fecha (string) a objeto date para comparar con la fecha de hoy
                fecha_reserva = datetime.strptime(r["fecha"], "%d/%m/%Y").date()
                if fecha_reserva >= hoy:
                    reservas_actualizadas.append(r)
            except ValueError:
                # Si alguna fecha está mal formateada se descarta
                continue

        # Sobrescribir el archivo con las reservas vigentes
        with open(RUTA_RESERVAS, "w", newline="") as archivo:
            campos = ["nombre", "personas", "fecha", "hora"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribimos encabezados y contenido
            escritor.writeheader()
            escritor.writerows(reservas_actualizadas)
    
    except FileNotFoundError:
        print("❌ No se encontró el archivo de reservas.")
    except Exception as e:
        print(f"❌ Error al borrar reservas: {e}")
    
def guardar_reserva(r):
    """
    Guarda una reserva en el archivo CSV.
    Si el archivo está vacío, agrega primero los encabezados.
    """
    try:
        with open(RUTA_RESERVAS, "a", newline="") as archivo:
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
    """
    Lee todas las reservas del archivo CSV y
    las devuelve como una lista de diccionarios.
    """
    try:
        with open(RUTA_RESERVAS, "r") as archivo:
            # Cada fila se lee como un diccionario
            lector = csv.DictReader(archivo)  
            reservas = list(lector)
            
            return reservas
    
    except FileNotFoundError:
        print("❌ No se encontró el archivo")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")