import menu
import reservas
import pedidos

def main():
    while True:
        print("=== RESTAURANTE ===")
        print("1. Ver la carta")
        print("2. Hacer una reserva")
        print("3. Hacer un pedido")
        print("4. Salir")
        
        try: 
            opcion = int(input("Elija una opción: ").strip())
        except ValueError:
            print("Por favor ingrese un número.\n")
            continue
        
        if opcion == 1:
            menu.mostrar_menu()
        elif opcion == 2:
            print("Reserva")
        elif opcion == 3:
            print("Pedido")
        elif opcion == 4:
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Ingrese un número entre 1 y 4\n")

if __name__ == "__main__":
    main()