import json
from tabulate import tabulate

def cargar_menu():
    try:
        with open("platos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo no se encuentra")
    except IOError:
        print("Problema para leer el archivo")

def mostrar_menu():
    platos = cargar_menu()
    print("--- MENÚ DE PLATOS ---")
    headers = ["", "Plato", "Precio"]
    tabla = [[p["id"], p["nombre"], p["precio"]] for p in platos]
    print(tabulate(tabla, headers, tablefmt="fancy_grid"))


