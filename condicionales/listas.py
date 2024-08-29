def menu():
    personas = []  

    while True:
        print("\nMenú:")
        print("1. Crear persona")
        print("2. Eliminar persona")
        print("3. Listar personas")
        print("4. Buscar persona")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la persona: ")
            personas.append(nombre)
            print("Lista actual de personas:", personas)

        elif opcion == "2":
            if not personas:
                print("La lista está vacía.")
                continue
            print("Lista de personas:")
            for i, persona in enumerate(personas):
                print(f"{i}. {persona}")
            try:
                indice = int(input("Seleccione el índice de la persona a eliminar: "))
                if 0 <= indice < len(personas):
                    eliminado = personas.pop(indice)
                    print(f"La persona '{eliminado}' ha sido eliminada.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")

        elif opcion == "3":
            if not personas:
                print("La lista está vacía.")
            else:
                print("Lista de personas:")
                for persona in personas:
                    print(persona)

        elif opcion == "4":
            if not personas:
                print("La lista está vacía.")
                continue
            busqueda = input("Ingrese el nombre de la persona a buscar: ")
            if busqueda in personas:
                print("La persona fue encontrada.")
            else:
                print("La persona no fue encontrada.")

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
