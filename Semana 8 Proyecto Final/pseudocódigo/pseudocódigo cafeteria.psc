Algoritmo SistemaCafeteria
	Definir usuario, nota Como Caracter
	Definir dia, mes, anio, opcion, opcionProd, cant, i, contVentas Como Entero
	Definir total, totalVentas Como Real
	Dimension ventas[100]
	Dimension prodNombre[4]
	Dimension prodPrecio[4]
	Dimension prodStock[4]
	
	prodNombre[1] = "Cafe"
	prodNombre[2] = "Te"
	prodNombre[3] = "Sandwich"
	prodNombre[4] = "Pastel"
	prodPrecio[1] = 35
	prodPrecio[2] = 25
	prodPrecio[3] = 50
	prodPrecio[4] = 40
	prodStock[1] = 10
	prodStock[2] = 10
	prodStock[3] = 5
	prodStock[4] = 5
	contVentas = 0
	totalVentas = 0
	
	Escribir "--- INICIANDO SISTEMA DE CAFETERIA ---"
	Esperar 1 Segundos
	Escribir "Sistema cargado con exito!"
	
	Escribir Sin Saltar "Ingresa tu nombre o nickname: "
	Leer usuario
	
	Escribir "Ingresa la fecha de operacion:"
	Escribir Sin Saltar "Dia: "
	Leer dia
	Escribir Sin Saltar "Mes: "
	Leer mes
	Escribir Sin Saltar "Anio: "
	Leer anio
	
	Repetir
		Escribir "======================================================="
		Escribir "SISTEMA CAFETERIA | Usuario: ", usuario
		Escribir "Fecha: ", dia, "/", mes, "/", anio
		Escribir "======================================================="
		Escribir "1. Registrar venta"
		Escribir "2. Corte de caja"
		Escribir "3. Ver stock actual"
		Escribir "4. Leer archivo txt"
		Escribir "5. Escribir en archivo"
		Escribir "6. Salir"
		Escribir "======================================================="
		Escribir Sin Saltar "Elige una opcion (1-6): "
		Leer opcion
		
		Segun opcion Hacer
			1:
				Escribir "--- REGISTRAR VENTA ---"
				Para i=1 Hasta 4 Con Paso 1 Hacer
					Escribir i, ". ", prodNombre[i], " - $", prodPrecio[i], " Stock ", prodStock[i]
				FinPara
				Escribir Sin Saltar "Elige producto (1-4): "
				Leer opcionProd
				Si opcionProd >=1 Y opcionProd <=4 Entonces
					Si prodStock[opcionProd] <=0 Entonces
						Escribir "Sin stock disponible."
					SiNo
						Escribir Sin Saltar "Cuantos deseas comprar?: "
						Leer cant
						Si cant >0 Y cant <= prodStock[opcionProd] Entonces
							prodStock[opcionProd] = prodStock[opcionProd] - cant
							total = prodPrecio[opcionProd] * cant
							contVentas = contVentas + 1
							ventas[contVentas] = total
							Escribir "Venta registrada. Total $", total
						SiNo
							Escribir "Cantidad no valida."
						FinSi
					FinSi
				SiNo
					Escribir "Producto no existe."
				FinSi
			2:
				totalVentas = 0
				Para i=1 Hasta contVentas Con Paso 1 Hacer
					totalVentas = totalVentas + ventas[i]
				FinPara
				Escribir "--- CORTE DE CAJA ---"
				Escribir "Ventas realizadas: ", contVentas
				Escribir "Total acumulado: $", totalVentas
				prodStock[1] = 10
				prodStock[2] = 10
				prodStock[3] = 5
				prodStock[4] = 5
				Escribir "Inventario reabastecido."
			3:
				Escribir "--- STOCK EN TIEMPO REAL ---"
				Para i=1 Hasta 4 Con Paso 1 Hacer
					Escribir prodNombre[i], " $", prodPrecio[i], " Disponibles ", prodStock[i]
				FinPara
			4:
				Escribir "--- ARCHIVOS DISPONIBLES ---"
				Escribir "1. ventas.txt 2. productos.txt 3. usuarios.txt 4. reportes.txt"
				Escribir "Simulacion: Contenido mostrado correctamente."
			5:
				Escribir Sin Saltar "Escribe tu nota: "
				Leer nota
				Escribir "Nota guardada: ", nota
			6:
				Escribir "Gracias por utilizar el sistema ", usuario
			De Otro Modo:
				Escribir "Opcion no valida."
		FinSegun
	Hasta Que opcion = 6
FinAlgoritmo