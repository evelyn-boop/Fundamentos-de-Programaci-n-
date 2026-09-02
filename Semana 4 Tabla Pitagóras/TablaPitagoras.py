#Actividad 4: Tabla de Pitágoras.
# Nombre: Evelyn Itzel León Uribe
# Matrícula: AL0731179
# Fecha: Viernes 04 de septiembre de 2026

# Crear la tabla de Pitágoras
tabla = []

for renglon in range(1, 11):
    fila = []

    for columna in range(1, 11):
        fila.append(renglon * columna)

    tabla.append(fila)

# Función para imprimir la tabla
def imprimir_tabla(tabla):

    for fila in tabla:

        for numero in fila:
            print(numero, end="\t")

        print()


# Función para consultar el resultado
def consultar_producto(tabla, renglon, columna):

    resultado = tabla[renglon - 1][columna - 1]

    return resultado 


# Mostrar la tabla
imprimir_tabla(tabla)


# Pedir los dos factores
renglon = int(input("\nIngresa el renglón: "))
columna = int(input("Ingresa la columna: "))


# Consultar el resultado en la matriz
resultado = consultar_producto(tabla, renglon, columna)

print("\nEl producto es:", resultado)