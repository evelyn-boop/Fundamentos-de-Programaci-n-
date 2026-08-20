# Actividad 2 - Cobro de entradas al museo

gratis = 0
menor = 30
adulto = 45

desc_adulto_mayor = 0.12
desc_profesor = 0.10
desc_estudiante = 0.10

total = 0

personas = int(input("¿Cuántas personas van a entrar al museo?: "))

# Tabla para que el usuario lo muestre tabulado
tabla = []

for persona in range(1, personas + 1):

    print("\nPersona", persona)

    edad = int(input("Ingresa la edad: "))

    # Si se ingresa una edad negativa, se termina el registro
    if edad < 0:
        print("La edad no puede ser negativa.")
        break

    if edad < 3:
        precio = gratis
        descuento_aplicado = 0
        pago = 0
        tipo_descuento = "Ninguno"

        print("La entrada es gratuita.")

        tabla.append([persona, edad, precio, tipo_descuento,
                      descuento_aplicado, pago])

        continue

    elif edad < 18:
        precio = menor

    else:
        precio = adulto

    print("\n¿Tiene algún descuento?")
    print("1 - Adulto mayor")
    print("2 - Profesor")
    print("3 - Estudiante")
    print("4 - Ninguno")

    opcion = input("Selecciona una opción: ")

    descuento = 0
    tipo_descuento = "Ninguno"

    if opcion == "1":
        descuento = desc_adulto_mayor
        tipo_descuento = "Adulto mayor"

    elif opcion == "2":
        descuento = desc_profesor
        tipo_descuento = "Profesor"

    elif opcion == "3":
        descuento = desc_estudiante
        tipo_descuento = "Estudiante"

    elif opcion == "4":
        descuento = 0

    else:
        print("Opción no válida.")
        print("Esta entrada no se registrará.")
        continue

    descuento_aplicado = precio * descuento
    pago = precio - descuento_aplicado

    total += pago

    tabla.append([persona, edad, precio, tipo_descuento,
                  descuento_aplicado, pago])

    print("\n--- Información de la entrada ---")
    print("Edad:", edad)
    print(f"Precio normal: ${precio:.2f}")
    print("Descuento:", tipo_descuento)
    print(f"Descuento aplicado: ${descuento_aplicado:.2f}")
    print(f"Total a pagar: ${pago:.2f}")


# Tabla final
print("\n==============================")
print("TABLA DE ENTRADAS")
print("==============================")

print("Persona | Edad | Precio | Descuento | Desc. aplicado | Total")

for fila in tabla:
    print(f"{fila[0]:7} | {fila[1]:4} | ${fila[2]:6.2f} | "
          f"{fila[3]:15} | ${fila[4]:13.2f} | ${fila[5]:6.2f}")

print("\n==============================")
print("TOTAL DE TODAS LAS ENTRADAS")
print(f"${total:.2f}")
print("==============================")