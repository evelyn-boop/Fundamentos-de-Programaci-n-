import time
import pdb

# Archivos de texto para almacenamiento
archivo_ventas = "ventas.txt"
archivo_productos = "productos.txt"
archivo_usuarios = "usuarios.txt"
archivo_reportes = "reportes.txt"

# Datos del sistema
Fecha = ()
usuario = ""

productos = {
    1: ["Café", 35.0, 10],
    2: ["Té", 25.0, 10],
    3: ["Sándwich", 50.0, 5],
    4: ["Pastel", 40.0, 5]
}

ventas = []


def pantalla_carga():
    print("\n--- INICIANDO SISTEMA DE CAFETERÍA ---")
    for i in range(1, 6):
        print(f"Cargando módulos del sistema... [{i}/5]")
        time.sleep(1)
    print("¡Sistema cargado e iniciado con éxito!\n")


def pedir_usuario():
    global usuario
    usuario = input("Ingresa tu nombre o nickname: ").strip()
    
    mensaje = "========================================\n"
    mensaje += "¡Hola, " + usuario + "! Bienvenido/a al sistema.\n"
    mensaje += "========================================"
    print(mensaje)


def pedir_fecha():
    global Fecha
    print("\nIngresa la fecha de operación:")
    dia = int(input("Día (ej. 25): "))
    mes = int(input("Mes (ej. 9): "))
    anio = int(input("Año (ej. 2026): "))
    
    Fecha = (dia, mes, anio)
    print(f"Fecha guardada en tupla correctamente: {Fecha}\n")


def crear_archivos_iniciales():
    try:
        with open(archivo_usuarios, "a", encoding="utf-8") as f:
            f.write(f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] Sesión iniciada por usuario: {usuario}\n")

        actualizar_archivo_productos()

        for nombre in [archivo_ventas, archivo_reportes]:
            with open(nombre, "a", encoding="utf-8") as f:
                pass
    except PermissionError:
        print("Error de acceso al crear archivos iniciales.")


def actualizar_archivo_productos():
    try:
        with open(archivo_productos, "w", encoding="utf-8") as f:
            f.write(f"--- INVENTARIO DE PRODUCTOS [{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] ---\n")
            for id_p, p in productos.items():
                f.write(f"ID: {id_p} | Nombre: {p[0]} | Precio: ${p[1]} | Stock: {p[2]} pzs\n")
    except PermissionError:
        print("Error de permisos al actualizar el inventario.")


def medir_inactividad():
    print("\n[CONTROL DE INACTIVIDAD DETECTADO]")
    print("Simulando conteo de 10 minutos sin interacción...")
    
    for minuto in range(1, 11):
        print(f"   Transcurriendo minuto {minuto} de 10...")
        time.sleep(0.1)
        
    print("\nHan transcurrido 10 minutos sin actividad.")
    respuesta = input("¿Deseas continuar en el menú principal? (si/no): ").strip().lower()
    
    if respuesta == "si":
        print("Continuando en el menú...\n")
        return True
    else:
        print("\nRegresando a la pantalla de inicio por inactividad. ¡Hasta luego!")
        return False


def registrar_venta():
    print("\n--- REGISTRAR VENTA ---")
    for id_p, p in productos.items():
        print(f"{id_p}. {p[0]} - ${p[1]} (Stock: {p[2]} pzs)")
        
    try:
        opcion = int(input("\nElige el número de producto (1-4): "))
        if opcion in productos:
            nombre = productos[opcion][0]
            precio = productos[opcion][1]
            stock = productos[opcion][2]
            
            if stock <= 0:
                print(f"Sin stock disponible de {nombre}.")
                return
                
            cant = int(input(f"¿Cuántos '{nombre}' deseas comprar? (Disponibles: {stock}): "))
            if cant <= 0 or cant > stock:
                print("Cantidad no válida.")
                return
                
            productos[opcion][2] = stock - cant
            total = precio * cant
            ventas.append(total)
            
            with open(archivo_ventas, "a", encoding="utf-8") as f:
                f.write(f"Fecha: {Fecha[0]}/{Fecha[1]}/{Fecha[2]} | Atendió: {usuario} | {nombre} x{cant} | Total: ${total}\n")
            
            actualizar_archivo_productos()
                
            print(f"Venta registrada con éxito. Total a pagar: ${total}")
        else:
            print("El producto no existe.")
    except ValueError:
        print("Error: Ingresa únicamente números enteros.")
    except PermissionError:
        print("Error: No se tienen permisos para modificar los archivos.")


def realizar_corte():
    print("\n--- CORTE DE CAJA ---")
    total_dinero = sum(ventas)
    print(f"Ventas realizadas en el turno: {len(ventas)}")
    print(f"Total dinero acumulado: ${total_dinero}")
    
    try:
        with open(archivo_reportes, "a", encoding="utf-8") as f:
            f.write(f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] CORTE DE CAJA | Atendió: {usuario} | Ventas: {len(ventas)} | Total acumulado: ${total_dinero}\n")
        
        productos[1][2] = 10
        productos[2][2] = 10
        productos[3][2] = 5
        productos[4][2] = 5
        
        actualizar_archivo_productos()
        print("Corte guardado en reportes.txt e inventario reabastecido.")
    except PermissionError:
        print("Error: Permisos denegados para guardar el reporte.")


def leer_archivo():
    print("\n--- ARCHIVOS DE TEXTO DISPONIBLES ---")
    archivos = {
        1: archivo_ventas,
        2: archivo_productos,
        3: archivo_usuarios,
        4: archivo_reportes
    }
    
    for num, nombre in archivos.items():
        print(f"{num}. {nombre}")
    
    try:
        opcion = int(input("Selecciona el número de archivo que deseas abrir (1-4): "))
        if opcion in archivos:
            nombre_archivo = archivos[opcion]
            
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                print(f"\n=== CONTENIDO DE {nombre_archivo} ===")
                texto = f.read()
                if texto.strip() == "":
                    print("(El archivo está vacío actualmente)")
                else:
                    print(texto)
                print("====================================")
        else:
            print("Esa opción no está en la lista.")
            
    except FileNotFoundError:
        print("Error: El archivo no existe en la carpeta.")
    except PermissionError:
        print("Error: No tienes permisos para leer este archivo.")
    except ValueError:
        print("Error: Debes ingresar un número entero.")


def escribir_archivo():
    print("\n--- ESCRIBIR / ANEXAR NOTA MANUAL EN ARCHIVO ---")
    archivos = {
        1: archivo_ventas,
        2: archivo_productos,
        3: archivo_usuarios,
        4: archivo_reportes
    }
    
    for num, nombre in archivos.items():
        print(f"{num}. {nombre}")
    
    try:
        opcion = int(input("Selecciona el archivo en el que deseas escribir (1-4): "))
        if opcion in archivos:
            nombre_archivo = archivos[opcion]
            nota = input("Escribe el texto que quieres agregar: ")
            
            with open(nombre_archivo, "a", encoding="utf-8") as f:
                f.write(f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] Nota de {usuario}: {nota}\n")
                
            print("Nota guardada correctamente.")
        else:
            print("Esa opción no existe.")
    except PermissionError:
        print("Error: No tienes permisos de escritura en este archivo.")
    except ValueError:
        print("Error: Entrada no válida.")


def main():
    pantalla_carga()
    pedir_usuario()
    pedir_fecha()
    crear_archivos_iniciales()

    matriz_menu = [
        ["1. Registrar venta", "2. Corte de caja"],
        ["3. Ver stock actual", "4. Leer archivo .txt"],
        ["5. Escribir en archivo", "6. Salir del programa"]
    ]

    opcion = 0
    while opcion != 6:
        print("\n=======================================================")
        print(f"SISTEMA CAFETERÍA | Usuario: {usuario} | Fecha: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}")
        print("=======================================================")

        for fila in matriz_menu:
            print(f"{fila[0]:<28} | {fila[1]}")
        print("=======================================================")

        entrada = input("\nElige una opción (1-6) o presiona ENTER para inactividad: ").strip()

        if entrada == "":
            continuar = medir_inactividad()
            if not continuar:
                break
            continue

        try:
            opcion = int(entrada)
        except ValueError:
            print("Error: Debes ingresar un número entero del 1 al 6.")
            continue

        # Descomentar para depurar con PDB
        #pdb.set_trace()

        if opcion == 1:
            registrar_venta()
        elif opcion == 2:
            realizar_corte()
        elif opcion == 3:
            print("\n--- STOCK EN TIEMPO REAL ---")
            for p in productos.values():
                print(f"• {p[0]}: ${p[1]} | Disponibles: {p[2]} pzs")
        elif opcion == 4:
            leer_archivo()
        elif opcion == 5:
            escribir_archivo()
        elif opcion == 6:
            print(f"\n¡Gracias por utilizar el sistema, {usuario}! Sesión finalizada.")
        else:
            print("Opción no válida. Intenta con un número del 1 al 6.")


if __name__ == "__main__":
    main()