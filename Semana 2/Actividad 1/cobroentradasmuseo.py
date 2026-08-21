# ****************************************************************************
# Actividad Evaluable 2 - Cobro de Entradas del Museo
# Nombre: Evelyn
# Fecha: 20 de agosto de 2026
# ****************************************************************************

# Constantes
PRECIO_MENOR_3 = 0
PRECIO_MENOR_EDAD = 30
PRECIO_ADULTO = 45

DESC_ADULTO_MAYOR = 0.12
DESC_PROFESOR = 0.10
DESC_ESTUDIANTE = 0.10
DESC_NINGUNO = 0.00

# Variables
total_general = 0.0
contador = 0

print("=== COBRO DE ENTRADAS - MUSEO DE ANTROPOLOGIA ===")
num_visitantes = int(input("Cuantos visitantes van a entrar? "))
print()

while contador < num_visitantes:
    contador += 1

    print(f" Visitante {contador}")
    edad = int(input("Edad: "))

    # Validar que la edad no sea negativa
    if edad < 0:
        print("La edad no puede ser negativa.")
        print()
        contador -= 1
        continue

    # Definir precio base
    if edad < 3:
        precio_base = PRECIO_MENOR_3
    elif edad >= 3 and edad <= 17:
        precio_base = PRECIO_MENOR_EDAD
    else:
        precio_base = PRECIO_ADULTO

    # Si es menor de 3 años no puede tener descuento
    if edad < 3:
        print("Es menor de 3 años, entrada gratis")
        descuento = DESC_NINGUNO
        monto_descuento = 0.0
        total = 0.0

        print(f"Precio base: ${precio_base:.2f}")
        print(f"Descuento: ${monto_descuento:.2f}")
        print(f"Total a pagar: ${total:.2f}")
        print()

        continue

    # Preguntar tipo solo si tiene 3 años o más
    print("Que tipo de visitante es?")
    print("1 - Adulto mayor (60+ años)")
    print("2 - Profesor")
    print("3 - Estudiante")
    print("4 - Ninguno")

    tipo = int(input("Elige una opcion: "))

    # Tabla de verdad, solo un descuento
    if tipo == 1 and edad >= 60:
        descuento = DESC_ADULTO_MAYOR
        nombre_descuento = "Adulto mayor 12%"

    elif tipo == 2 and edad >= 18:
        descuento = DESC_PROFESOR
        nombre_descuento = "Profesor 10%"

    elif tipo == 3:
        descuento = DESC_ESTUDIANTE
        nombre_descuento = "Estudiante 10%"

    elif tipo == 4:
        descuento = DESC_NINGUNO
        nombre_descuento = "Sin descuento"

    else:
        print("No puedes usar ese descuento por tu edad")
        descuento = DESC_NINGUNO
        nombre_descuento = "Sin descuento"

    # Calcular
    monto_descuento = precio_base * descuento
    total = precio_base - monto_descuento

    # Acumular
    total_general += total

    # Mostrar datos del visitante
    print(f"Precio base: ${precio_base:.2f}")
    print(f"Descuento aplicado: {nombre_descuento}")
    print(f"Monto del descuento: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print()

# Resumen final
print("========================================")
print(f"TOTAL GENERAL: ${total_general:.2f}")
print("========================================")