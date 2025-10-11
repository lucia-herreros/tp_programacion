import json

def mostrar_menu():
    try:
        with open("datos/platos.json", "r") as archivo:
            platos = json.load(archivo)

            tamaño_columna_id = 8
            tamaño_columna = 30
            titulo = "--- MENÚ DE PLATOS ---"
            headers = [" ", "Plato", "Precio"]
            
            print(titulo)
            
            # Imprimir línea divisoria
            print("|" + ("-" * tamaño_columna_id) + "|" + ("-" * tamaño_columna + "|") * 2)

            # Imprimir encabezados
            print(f"|{headers[0]:^{tamaño_columna_id}}|{headers[1]:^{tamaño_columna}}|{headers[2]:^{tamaño_columna}}|")

            # Imprimir segunda línea divisoria
            print("|" + ("-" * tamaño_columna_id) + "|" + ("-" * tamaño_columna + "|") * 2)

            # Imprimir cada plato
            for plato in platos:
                print(f"|{plato['id']:^{tamaño_columna_id}}|{plato['nombre']:^{tamaño_columna}}|{plato['precio']:^{tamaño_columna}}|")
            
            # Imprimir línea divisoria final
            print("|" + ("-" * tamaño_columna_id) + "|" + ("-" * tamaño_columna + "|") * 2)
    except FileNotFoundError:
        print("El archivo no se encuentra")
    except json.JSONDecodeError:
        print("Problema para decodificar JSON")
    finally:
        try:
            archivo.close()
        except NameError:
            pass