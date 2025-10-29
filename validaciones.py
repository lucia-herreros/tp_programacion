def pedir_nombre():
    nombre = input("Ingrese su nombre: ").strip()
    if len(nombre) < 3 or not all(c.isalpha() or c.isspace() for c in nombre):
        print("❌ Nombre inválido. Intente de nuevo.")
        return pedir_nombre()  # La función vuelve a llamarse a sí misma
    return nombre

