import menu
import reservas
import pedidos

def main():
    while True:
        print("\n=== RESTAURANTE ===")
        print("1. Ver la carta")
        print("2. Hacer una reserva")
        print("3. Hacer un pedido")
        print("4. Ver reservas")
        print("5. Salir")
        
        try: 
            opcion = int(input("Elija una opción: ").strip())
        except ValueError:
            print("⚠️ Por favor ingrese un número.\n")
            continue
        
        if opcion == 1:
            menu.mostrar_menu()
        elif opcion == 2:
            reservas.hacer_reserva()
        elif opcion == 3:
            pedidos.hacer_pedido()
        elif opcion == 4:
            reservas.mostrar_reservas()
        elif opcion == 5:
            print("\n¡Hasta pronto!\n")
            break
        else:
            print("❌ Opción inválida. Ingrese un número entre 1 y 5\n")

if __name__ == "__main__":
    main()
