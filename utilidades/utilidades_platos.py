import json

RUTA_PLATOS = "datos/platos.json"

def cargar_platos():
    """Devuelve la lista de platos desde el archivo JSON."""
    try:
        with open(RUTA_PLATOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Error: El archivo de platos no existe.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo de platos tiene formato inválido.")
        return []
