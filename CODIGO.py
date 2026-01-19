# Programa sencillo para gestionar una lista de tareas

tareas = []

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Escribe la nueva tarea: ")
        tareas.append(tarea)
        print("Tarea agregada correctamente")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas pendientes")
        else:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para eliminar")
        else:
            numero = int(input("Número de la tarea a eliminar: "))
            if 1 <= numero <= len(tareas):
                tareas.pop(numero - 1)
                print("Tarea eliminada")
            else:
                print("Número inválido")

    elif opcion == "4":
        print("Saliendo del programa")
        break

    else:
        print("Opción no válida")
