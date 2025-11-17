from utilidades.utilidades_platos import cargar_platos

def mostrar_menu():
    platos = cargar_platos()

    tamaño_columna_id = 8
    tamaño_columna = 30
    titulo = "--- MENÚ DE PLATOS ---"
    headers = [" ", "Plato", "Precio"]
    
    print(f"\n{titulo}")
    
    # Imprimir línea divisoria
    print("|" + ("-" * tamaño_columna_id) + "|" + ("-" * tamaño_columna + "|") * 2)

    # Imprimir encabezados
    print(f"|{headers[0]:^{tamaño_columna_id}}|{headers[1]:^{tamaño_columna}}|{headers[2]:^{tamaño_columna}}|")

    # Imprimir segunda línea divisoria
    print("|" + ("-" * tamaño_columna_id) + "|" + ("-" * tamaño_columna + "|") * 2)

    # Imprimir cada plato
    for plato in platos:
        print(f"|{plato['id']:^{tamaño_columna_id}}|{plato['nombre']:^{tamaño_columna}}|{"$" + str(plato['precio']):^{tamaño_columna}}|")
    
    # Imprimir línea divisoria final
    print("|" + ("-" * tamaño_columna_id) + "|" + ("-" * tamaño_columna + "|") * 2)
