# Lista para almacenar productos
inventario = []

# Menú interactivo
while True:
    print("\nMenú de Gestión de Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario.append({"nombre": nombre, "cantidad": cantidad})
        print(f"Producto {nombre} agregado con éxito.")
    elif opcion == "2":
        if inventario:
            print("Productos en inventario:")
            for producto in inventario:
                print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
        else:
            print("El inventario está vacío.")
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
