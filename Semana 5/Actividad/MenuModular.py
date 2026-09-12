# ==========================================
# SECCIÓN 1: TRABAJO CON TUPLAS
#Actividad Semana 5 MenuModular 
#Evelyn Itzel León Uribe 
#Matricula: AL07311179
# ==========================================

# Función que recibe la tupla y retorna la suma de sus elementos
def sumar_calificaciones(tupla_notas):
    suma_total = sum(tupla_notas)
    return suma_total


# 1. Crear tupla inicial con 5 calificaciones
calificaciones = (85, 90, 78, 92, 88)
print("--- REGISTRO DE CALIFICACIONES ---")
print("Calificaciones iniciales:", calificaciones)

# 2. Acceder e imprimir el tercer elemento (índice 2)
print("La calificación del tercer parcial es:", calificaciones[2])

# 3. Capturar dos calificaciones adicionales con input()
nota1 = float(input("Ingresa la calificación de la Tarea 1: "))
nota2 = float(input("Ingresa la calificación de la Tarea 2: "))

# Anexar los datos para crear una nueva tupla
todas_las_notas = calificaciones + (nota1, nota2)
print("Nueva tupla con todas las notas:", todas_las_notas)

# 4. Convertir la tupla a lista y ordenarla
lista_notas = list(todas_las_notas)
lista_notas.sort()
print("Calificaciones ordenadas de menor a mayor:", lista_notas)

# 5. Llamar a la función que suma los elementos y muestra el retorno
total_puntos = sumar_calificaciones(todas_las_notas)
print("El total de puntos acumulados es:", total_puntos)