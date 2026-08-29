# SISTEMA DE VENTAS PARA CAFETERÍA "BUEN CAFÉ"
# Desarrollo del programa hasta el RF06
# En esta etapa solamente se implementan las funciones RF01 a RF06


# RF04 - Productos disponibles
# Se utiliza un diccionario para almacenar los productos de la cafetería
# Cada producto tiene un número, un nombre y un precio
productos = {
    1: ("Cafe", 35.00),
    2: ("Te", 25.00),
    3: ("Sandwich", 50.00),
    4: ("Pastel", 40.00)
}


# Se crea una variable para controlar la opción seleccionada
# El valor inicial es cero para poder iniciar el ciclo del menú
opcion = 0


# RF01 - Mostrar el menú principal
# RF02 - Permitir seleccionar una opción
# El ciclo se mantiene activo mientras el usuario no seleccione salir
while opcion != 4:

    # Se muestran líneas para separar visualmente el menú
    print("================================")

    # Se muestra el nombre de la cafetería
    print("       CAFETERIA BUEN CAFE")

    # Se vuelve a colocar una línea para mejorar la presentación
    print("================================")

    # Opción para registrar una nueva venta
    print("1. Registrar venta")

    # Opción para consultar el total de ventas
    # Esta función se implementará posteriormente
    print("2. Ver total de ventas")

    # Opción para consultar la cantidad de ventas
    # Esta función se implementará posteriormente
    print("3. Ver cantidad de ventas")

    # Opción para terminar el programa
    print("4. Salir")

    # Se muestra una línea al final del menú
    print("================================")

    # Se solicita al usuario que seleccione una opción
    # int permite guardar la respuesta como un número entero
    opcion = int(input("Seleccione una opcion: "))


    # RF03 - Registrar una nueva venta
    # Si el usuario selecciona la opción 1 se inicia el registro
    # de una nueva venta
    if opcion == 1:

        # Se muestra el título de los productos disponibles
        print("\nPRODUCTOS DISPONIBLES")


        # RF04 - Mostrar los productos disponibles
        # El ciclo for recorre todos los productos del diccionario
        # numero representa el número del producto
        # datos contiene el nombre y el precio
        for numero, datos in productos.items():

            # Se muestra el número, nombre y precio del producto
            # :.2f permite mostrar el precio con dos decimales
            print(f"{numero}. {datos[0]} - ${datos[1]:.2f}")


        # RF05 - Seleccionar un producto
        # Se solicita al usuario el número del producto que desea
        producto = int(input("\nSeleccione un producto: "))


        # Se verifica que el número seleccionado exista
        # dentro de los productos disponibles
        if producto in productos:

            # Se obtienen el nombre y el precio del producto seleccionado
            nombre_producto, precio = productos[producto]

            # Se muestra el nombre del producto elegido
            print(f"\nProducto seleccionado: {nombre_producto}")

            # Se muestra el precio del producto seleccionado
            print(f"Precio: ${precio:.2f}")


            # RF06 - Registrar la cantidad de productos
            # Se solicita al usuario la cantidad que desea comprar
            cantidad = int(input("Ingrese la cantidad: "))


            # Se verifica que la cantidad ingresada sea mayor que cero
            if cantidad > 0:

                # Se muestran líneas para indicar que la venta fue registrada
                print("\n================================")

                # Se informa que la venta fue capturada correctamente
                print("VENTA CAPTURADA CORRECTAMENTE")

                # Se muestra otra línea para separar la información
                print("================================")

                # Se muestra el producto seleccionado
                print(f"Producto: {nombre_producto}")

                # Se muestra la cantidad registrada
                print(f"Cantidad: {cantidad}")

                # Se muestra una línea al final de la información
                print("================================")

            # Si la cantidad es cero o negativa, se muestra un mensaje
            else:
                print("La cantidad debe ser mayor que cero.")


        # Si el producto seleccionado no existe
        # se informa al usuario que la opción no es válida
        else:
            print("Producto no valido.")


    # RF07 en adelante todavía NO se implementan
    # Estas funciones quedan pendientes para una siguiente etapa

    # Si se selecciona la opción 2, todavía no se calcula el total
    elif opcion == 2:

        # Se informa que esta función será agregada posteriormente
        print("\nEsta funcion se implementara posteriormente.")


    # Si se selecciona la opción 3, todavía no se calcula la cantidad
    elif opcion == 3:

        # Se informa que esta función será agregada posteriormente
        print("\nEsta funcion se implementara posteriormente.")


    # Si el usuario selecciona la opción 4
    # el ciclo while terminará
    elif opcion == 4:

        # Se muestra un mensaje indicando que el programa terminó
        print("\nPrograma finalizado.")


    # Si el usuario escribe una opción diferente de 1, 2, 3 o 4
    # se muestra un mensaje indicando que la opción no es válida
    else:

        # Mensaje para indicar que la opción seleccionada no existe
        print("\nOpcion no valida.")