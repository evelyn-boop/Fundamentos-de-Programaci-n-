# SISTEMA DE VENTAS PARA CAFETERÍA "BUEN CAFÉ"
# Desarrollo hasta RF06 

# RF04 - Productos disponibles 
productos = {
    1: ("Cafe", 35.00),
    2: ("Te", 25.00),
    3: ("Sandwich", 50.00),
    4: ("Pastel", 40.00)
}  

# Variable para controlar el menú 
opcion = 0  

# RF01 - Mostrar el menú principal
# RF02 - Permitir seleccionar una opción
while opcion != 4: 
 
    print("================================")
    print("       CAFETERIA BUEN CAFE")
    print("================================")
    print("1. Registrar venta")
    print("2. Ver total de ventas") 
    print("3. Ver cantidad de ventas")
    print("4. Salir")
    print("================================")

    opcion = int(input("Seleccione una opcion: "))

    # RF03 - Registrar una nueva venta
    if opcion == 1:

        print("\nPRODUCTOS DISPONIBLES")

        # RF04 - Mostrar los productos disponibles
        for numero, datos in productos.items():
            print(f"{numero}. {datos[0]} - ${datos[1]:.2f}")

        # RF05 - Seleccionar un producto
        producto = int(input("\nSeleccione un producto: "))

        if producto in productos:

            nombre_producto, precio = productos[producto]

            print(f"\nProducto seleccionado: {nombre_producto}")
            print(f"Precio: ${precio:.2f}")

            # RF06 - Registrar la cantidad de productos
            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad > 0:
                print("\n================================")
                print("VENTA CAPTURADA CORRECTAMENTE")
                print("================================")
                print(f"Producto: {nombre_producto}")
                print(f"Cantidad: {cantidad}")
                print("================================")

            else:
                print("La cantidad debe ser mayor que cero.")

        else:
            print("Producto no valido.")

    # RF07 en adelante todavía NO se implementan
    elif opcion == 2:
        print("\nEsta funcion se implementara posteriormente.")

    elif opcion == 3:
        print("\nEsta funcion se implementara posteriormente.")

    # Salir
    elif opcion == 4:
        print("\nPrograma finalizado.")

    else:
        print("\nOpcion no valida.")