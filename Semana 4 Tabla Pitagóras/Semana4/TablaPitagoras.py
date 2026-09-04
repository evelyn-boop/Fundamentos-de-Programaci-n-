# Nombre: Evelyn Itzel León Uribe 
# Matrícula: AL0731179 
# Fecha: Viernes 04 de Septiembre de 2026 
 
# Se crea una lista vacía para guardar la tabla de Pitágoras 
tabla = [] 
# Se hace el llenado de la tabla de Pitágoras 
# con los resultados de la multiplicación de los números del 1 al 10 
for renglon in range(1, 11): 
 
    # Se crea una lista para guardar cada renglon 
    fila = [] 
 
    for columna in range(1, 11): 
 
        # Se multiplica el renglon por la columna 
        resultado = renglon * columna 
 
        # Se agrega el resultado a la fila 
        fila.append(resultado) 
 
    # Se agrega la fila a la tabla 
    tabla.append(fila) 
 
 
# Se crea una función para mostrar la tabla de Pitágoras 
def mostrar_tabla(tabla): 
 
    # Se muestran los números de las columnas 
    print("  " , end="\t") 
 
    for columna in range(1, 11): 
        print(columna, end="\t") 
 
    print() 
 
    # Se muestra una línea para separar 
    print("  " and "-" * 85) 
 
    # Se muestran los renglones de la tabla 
    numero = 1 
 
    for fila in tabla: 
 
        # Se muestra el número del renglon 
        print(numero, end="\t") 
 
        # Se muestran los resultados 
        for valor in fila: 
            print(valor, end="\t") 
 
        print() 
 
        # Se aumenta el número del renglon 
        numero += 1 
 
 
# Se crea una función para realizar la multiplicación 
def multiplicar(tabla, factor1, factor2): 
 
    # Se busca el primer factor en los renglones 
    numero = 1 
 
    for fila in tabla: 
         
        if numero == factor1: 
 
            # Se busca el segundo factor en la fila 
            columna = 1 
 
            for valor in fila: 
 
                if columna == factor2: 
 
                    return valor 
 
                columna += 1 
 
        numero += 1 
 
 
# Se muestra la tabla de Pitágoras 
print("TABLA DE PITÁGORAS") 
print() 
 
mostrar_tabla(tabla) 
 
 
# Se solicitan los dos factores al usuario 
print() 
factor1 = int(input("Ingresa el primer factor: ")) 
factor2 = int(input("Ingresa el segundo factor: ")) 
 
 
# Se verifica que los factores estén entre 1 y 10 
if factor1 >= 1 and factor1 <= 10 and factor2 >= 1 and factor2 <= 10: 
 
    # Se obtiene el resultado de la multiplicación 
    resultado = multiplicar(tabla, factor1, factor2) 
 
    # Se muestra el resultado 
    print() 
    print("El resultado de la multiplicación es:", resultado) 
 
else: 
 
    # Se muestra un mensaje si los factores no son válidos 
    print() 
    print("Los factores deben estar entre 1 y 10.")