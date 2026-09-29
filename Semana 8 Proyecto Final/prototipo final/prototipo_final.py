import time
import pdb
from datetime import datetime


# ============================================================
# ARCHIVOS DE TEXTO
# ============================================================

archivo_ventas = "ventas.txt"
archivo_productos = "productos.txt"
archivo_usuarios = "usuarios.txt"
archivo_reportes = "reportes.txt"


# ============================================================
# DATOS DEL SISTEMA
# ============================================================

Fecha = ()
usuario = ""


# ============================================================
# PRODUCTOS DE LA CAFETERÍA
# ============================================================

productos = {
    1: ["Café", 35.0, 10],
    2: ["Té", 25.0, 10],
    3: ["Sándwich", 50.0, 5],
    4: ["Pastel", 40.0, 5]
}


# Lista para almacenar las ventas del turno
ventas = []


# ============================================================
# PANTALLA DE CARGA
# ============================================================

def pantalla_carga():
    print("\n--- INICIANDO SISTEMA DE CAFETERÍA ---")

    # Espera de 5 segundos
    for i in range(1, 6):
        print(f"Cargando módulos del sistema... [{i}/5]")
        time.sleep(1)

    print("¡Sistema cargado e iniciado con éxito!\n")


# ============================================================
# PEDIR USUARIO
# ============================================================

def pedir_usuario():
    global usuario

    while True:
        usuario = input(
            "Ingresa tu nombre o nickname: "
        ).strip()

        if usuario != "":
            break

        print(
            "Error: Debes ingresar un nombre o nickname."
        )

    mensaje = "========================================\n"
    mensaje += (
        "¡Hola, " + usuario +
        "! Bienvenido/a al sistema.\n"
    )
    mensaje += "========================================"

    print(mensaje)


# ============================================================
# PEDIR Y VALIDAR FECHA
# ============================================================

def pedir_fecha():
    global Fecha

    print("\nIngresa la fecha de operación:")

    while True:
        try:
            dia = int(
                input("Día (ej. 25): ")
            )

            mes = int(
                input("Mes (ej. 9): ")
            )

            anio = int(
                input("Año (ej. 2026): ")
            )

            # Validar que el año tenga 4 dígitos
            if anio < 1000 or anio > 9999:
                print(
                    "Error: El año debe tener "
                    "4 dígitos."
                )
                continue

            # Python valida automáticamente:
            # - días de cada mes
            # - meses del 1 al 12
            # - años bisiestos
            fecha_valida = datetime(
                anio,
                mes,
                dia
            )

            # Guardar fecha como tupla
            Fecha = (dia, mes, anio)

            print(
                f"Fecha válida y guardada "
                f"correctamente: {Fecha}\n"
            )

            break

        except ValueError:
            print(
                "Error: La fecha ingresada no es válida. "
                "Verifica el día, mes y año."
            )


# ============================================================
# CREAR ARCHIVOS INICIALES
# ============================================================

def crear_archivos_iniciales():

    try:

        with open(
            archivo_usuarios,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] "
                f"Sesión iniciada por usuario: "
                f"{usuario}\n"
            )

        actualizar_archivo_productos()

        for nombre in [
            archivo_ventas,
            archivo_reportes
        ]:

            with open(
                nombre,
                "a",
                encoding="utf-8"
            ):
                pass

    except PermissionError:
        print(
            "Error de acceso al crear "
            "archivos iniciales."
        )


# ============================================================
# ACTUALIZAR ARCHIVO DE PRODUCTOS
# ============================================================

def actualizar_archivo_productos():

    try:

        with open(
            archivo_productos,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                f"--- INVENTARIO DE PRODUCTOS "
                f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] ---\n"
            )

            for id_p, p in productos.items():

                f.write(
                    f"ID: {id_p} | "
                    f"Nombre: {p[0]} | "
                    f"Precio: ${p[1]} | "
                    f"Stock: {p[2]} pzs\n"
                )

    except PermissionError:
        print(
            "Error de permisos al actualizar "
            "el inventario."
        )


# ============================================================
# CONTROL DE INACTIVIDAD
# ============================================================

def medir_inactividad():

    print("\n--- CONTROL DE INACTIVIDAD ---")
    print("No se detectó actividad.")
    print("El sistema esperará 10 minutos.")

    for minuto in range(1, 11):

        print(
            f"Transcurriendo minuto {minuto} de 10..."
        )

        time.sleep(60)

    print(
        "\nHan transcurrido 10 minutos "
        "sin actividad."
    )

    respuesta = input(
        "¿Deseas continuar en el menú principal? "
        "(si/no): "
    ).strip().lower()

    if respuesta == "si":

        print(
            "Continuando en el menú...\n"
        )

        return True

    else:

        print(
            "\nRegresando a la pantalla de inicio. "
            "¡Hasta luego!"
        )

        return False


# ============================================================
# REGISTRAR VENTA
# ============================================================

def registrar_venta():

    print("\n--- REGISTRAR VENTA ---")

    for id_p, p in productos.items():

        print(
            f"{id_p}. {p[0]} - ${p[1]} "
            f"(Stock: {p[2]} pzs)"
        )

    try:

        opcion = int(
            input(
                "\nElige el número de producto (1-4): "
            )
        )

        if opcion in productos:

            nombre = productos[opcion][0]
            precio = productos[opcion][1]
            stock = productos[opcion][2]

            if stock <= 0:

                print(
                    f"Sin stock disponible de {nombre}."
                )

                return

            cant = int(
                input(
                    f"¿Cuántos '{nombre}' deseas comprar? "
                    f"(Disponibles: {stock}): "
                )
            )

            if cant <= 0 or cant > stock:

                print(
                    "Cantidad no válida."
                )

                return

            # Descontar stock
            productos[opcion][2] = stock - cant

            # Calcular total
            total = precio * cant

            # Guardar venta en la lista
            ventas.append(total)

            # Guardar venta en archivo
            with open(
                archivo_ventas,
                "a",
                encoding="utf-8"
            ) as f:

                f.write(
                    f"Fecha: "
                    f"{Fecha[0]}/{Fecha[1]}/{Fecha[2]} | "
                    f"Atendió: {usuario} | "
                    f"{nombre} x{cant} | "
                    f"Total: ${total}\n"
                )

            # Actualizar inventario
            actualizar_archivo_productos()

            print(
                f"Venta registrada con éxito. "
                f"Total a pagar: ${total}"
            )

        else:

            print(
                "El producto no existe."
            )

    except ValueError:

        print(
            "Error: Ingresa únicamente "
            "números enteros."
        )

    except PermissionError:

        print(
            "Error: No se tienen permisos "
            "para modificar los archivos."
        )


# ============================================================
# CORTE DE CAJA
# ============================================================

def realizar_corte():

    print("\n--- CORTE DE CAJA ---")

    total_dinero = sum(ventas)

    print(
        f"Ventas realizadas en el turno: "
        f"{len(ventas)}"
    )

    print(
        f"Total dinero acumulado: "
        f"${total_dinero}"
    )

    try:

        with open(
            archivo_reportes,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] "
                f"CORTE DE CAJA | "
                f"Atendió: {usuario} | "
                f"Ventas: {len(ventas)} | "
                f"Total acumulado: ${total_dinero}\n"
            )

        # Reabastecer inventario
        productos[1][2] = 10
        productos[2][2] = 10
        productos[3][2] = 5
        productos[4][2] = 5

        actualizar_archivo_productos()

        print(
            "Corte guardado en reportes.txt "
            "e inventario reabastecido."
        )

    except PermissionError:

        print(
            "Error: Permisos denegados "
            "para guardar el reporte."
        )


# ============================================================
# LEER ARCHIVO
# ============================================================

def leer_archivo():

    print(
        "\n--- ARCHIVOS DE TEXTO DISPONIBLES ---"
    )

    archivos = {
        1: archivo_ventas,
        2: archivo_productos,
        3: archivo_usuarios,
        4: archivo_reportes
    }

    for num, nombre in archivos.items():

        print(
            f"{num}. {nombre}"
        )

    try:

        opcion = int(
            input(
                "Selecciona el número de archivo "
                "que deseas abrir (1-4): "
            )
        )

        if opcion in archivos:

            nombre_archivo = archivos[opcion]

            with open(
                nombre_archivo,
                "r",
                encoding="utf-8"
            ) as f:

                print(
                    f"\n=== CONTENIDO DE "
                    f"{nombre_archivo} ==="
                )

                texto = f.read()

                if texto.strip() == "":

                    print(
                        "(El archivo está vacío actualmente)"
                    )

                else:

                    print(texto)

                print(
                    "===================================="
                )

        else:

            print(
                "Esa opción no está en la lista."
            )

    except FileNotFoundError:

        print(
            "Error: El archivo no existe "
            "en la carpeta."
        )

    except PermissionError:

        print(
            "Error: No tienes permisos "
            "para leer este archivo."
        )

    except ValueError:

        print(
            "Error: Debes ingresar "
            "un número entero."
        )


# ============================================================
# ESCRIBIR EN ARCHIVO
# ============================================================

def escribir_archivo():

    print(
        "\n--- ESCRIBIR / ANEXAR NOTA "
        "MANUAL EN ARCHIVO ---"
    )

    archivos = {
        1: archivo_ventas,
        2: archivo_productos,
        3: archivo_usuarios,
        4: archivo_reportes
    }

    for num, nombre in archivos.items():

        print(
            f"{num}. {nombre}"
        )

    try:

        opcion = int(
            input(
                "Selecciona el archivo "
                "en el que deseas escribir (1-4): "
            )
        )

        if opcion in archivos:

            nombre_archivo = archivos[opcion]

            nota = input(
                "Escribe el texto que quieres agregar: "
            )

            with open(
                nombre_archivo,
                "a",
                encoding="utf-8"
            ) as f:

                f.write(
                    f"[{Fecha[0]}/{Fecha[1]}/{Fecha[2]}] "
                    f"Nota de {usuario}: {nota}\n"
                )

            print(
                "Nota guardada correctamente."
            )

        else:

            print(
                "Esa opción no existe."
            )

    except PermissionError:

        print(
            "Error: No tienes permisos "
            "de escritura en este archivo."
        )

    except ValueError:

        print(
            "Error: Entrada no válida."
        )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    # Pantalla de carga
    pantalla_carga()

    # Solicitar usuario y fecha
    pedir_usuario()
    pedir_fecha()

    # Crear archivos iniciales
    crear_archivos_iniciales()

    # ========================================================
    # MATRIZ DEL MENÚ
    # ========================================================

    matriz_menu = [
        [
            "1. Registrar venta",
            "2. Corte de caja"
        ],
        [
            "3. Ver stock actual",
            "4. Leer archivo .txt"
        ],
        [
            "5. Escribir en archivo",
            "6. Cambiar de usuario"
        ],
        [
            "7. Salir del programa",
            ""
        ]
    ]

    opcion = 0

    # ========================================================
    # CICLO DEL MENÚ
    # ========================================================

    while opcion != 7:

        print(
            "\n======================================================="
        )

        print(
            f"SISTEMA CAFETERÍA | "
            f"Usuario: {usuario} | "
            f"Fecha: "
            f"{Fecha[0]}/{Fecha[1]}/{Fecha[2]}"
        )

        print(
            "======================================================="
        )

        # Mostrar matriz
        for fila in matriz_menu:

            print(
                f"{fila[0]:<28} | {fila[1]}"
            )

        print(
            "======================================================="
        )

        entrada = input(
            "\nElige una opción (1-7) "
            "o presiona ENTER para inactividad: "
        ).strip()

        # ====================================================
        # INACTIVIDAD
        # ====================================================

        if entrada == "":

            continuar = medir_inactividad()

            if not continuar:
                break

            continue

        # ====================================================
        # VALIDAR OPCIÓN
        # ====================================================

        try:

            opcion = int(entrada)

        except ValueError:

            print(
                "Error: Debes ingresar "
                "un número entero del 1 al 7."
            )

            continue

        # ====================================================
        # DEPURACIÓN CON PDB
        # ====================================================

        # Descomenta esta línea cuando hagas
        # la evidencia de depuración:
        # pdb.set_trace()

        # ====================================================
        # OPCIÓN 1
        # ====================================================

        if opcion == 1:

            registrar_venta()

        # ====================================================
        # OPCIÓN 2
        # ====================================================

        elif opcion == 2:

            realizar_corte()

        # ====================================================
        # OPCIÓN 3
        # ====================================================

        elif opcion == 3:

            print(
                "\n--- STOCK EN TIEMPO REAL ---"
            )

            for p in productos.values():

                print(
                    f"• {p[0]}: ${p[1]} | "
                    f"Disponibles: {p[2]} pzs"
                )

        # ====================================================
        # OPCIÓN 4
        # ====================================================

        elif opcion == 4:

            leer_archivo()

        # ====================================================
        # OPCIÓN 5
        # ====================================================

        elif opcion == 5:

            escribir_archivo()

        # ====================================================
        # OPCIÓN 6
        # ====================================================

        elif opcion == 6:

            print(
                "\n--- CAMBIO DE USUARIO ---"
            )

            pedir_usuario()

            print(
                f"Usuario actualizado correctamente: "
                f"{usuario}"
            )

        # ====================================================
        # OPCIÓN 7
        # ====================================================

        elif opcion == 7:

            print(
                f"\n¡Gracias por utilizar el sistema, "
                f"{usuario}!"
            )

            print(
                "Sesión finalizada."
            )

        # ====================================================
        # OPCIÓN NO VÁLIDA
        # ====================================================

        else:

            print(
                "Opción no válida. "
                "Intenta con un número del 1 al 7."
            )


# ============================================================
# EJECUTAR PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()