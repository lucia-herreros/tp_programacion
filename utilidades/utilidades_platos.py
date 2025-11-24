import json

RUTA_PLATOS = "datos/platos.json"

def cargar_platos():
    """
    Carga y devuelve la lista de platos desde el archivo JSON.
    Si hay algún error, devuelve una lista vacía.
    """
    try:
        # Intentamos abrir el archivo y convertir su contenido en una lista de diccionarios
        with open(RUTA_PLATOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("❌ Error: El archivo de platos no existe.")
        return []
    except json.JSONDecodeError:
        print("❌ Error: El archivo de platos tiene formato inválido.")
        return []
    except Exception as e:
        print("❌ Error al cargar los platos:", e)
        return []

def guardar_platos(platos):
    """
    Guarda la lista de platos en el archivo JSON.
    Devuelve True si se guardó correctamente.
    """
    try:
        with open(RUTA_PLATOS, "w") as archivo:
            json.dump(platos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print("❌ Error al guardar los platos:", e)
        return False

def generar_nuevo_id(platos):
    """
    Genera un ID nuevo y único basado en el ID más alto encontrado.
    Si no hay platos, el ID comienza en 1.
    """
    try:
        if not platos:
            return 1
        # Busca el ID más alto y se suma 1
        return max(p["id"] for p in platos) + 1
    except Exception as e:
        print("❌ Error al generar ID:", e)
        return None

def agregar_plato(nombre, precio):
    """
    Agrega un nuevo plato al archivo JSON.
    Antes de agregar, verifica mediante un conjunto
    que no exista otro plato con el mismo nombre.
    Devuelve True se logró agregar el plato.
    """
    try:
        platos = cargar_platos()

        # Si no hay platos todavía, comenzamos con lista vacía
        if not platos:
            platos = []
        
        # Conjunto con los nombres ya existentes en minúscula
        platos_existentes = {p["nombre"].lower() for p in platos}

        # Si el nombre ya está en el conjunto, no se agrega
        if nombre.lower() in platos_existentes:
            print("⚠️ Ya existe un plato con ese nombre.")
            return False  
        
        nuevo_id = generar_nuevo_id(platos)

        if not nuevo_id:
            return False

        # Estructura del nuevo plato
        nuevo_plato = {
            "id": nuevo_id,
            "nombre": nombre,
            "precio": precio
        }

        # Se agrega el plato a la lista y se guarda el archivo actualizado
        platos.append(nuevo_plato)
        guardar_platos(platos)

        return True    
    except Exception as e:
        print("❌ Error al crear el nuevo plato:", e)
        return False

def mostrar_menu_simple():
    """
    Muestra los platos cargados en el archivo de forma simple.
    Si no hay platos, se informa al usuario.
    """
    
    platos = cargar_platos()
    if not platos:
        print("⚠️ La carta está vacía.")
        return
    
    for p in platos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']}")