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