Algoritmo Sistema_Cafeteria
    Definir opcion, producto, cantidad Como Entero
    Definir nombre_producto Como Caracter
	
    Mientras opcion <> 4 Hacer
        Escribir "================================"
        Escribir "       CAFETERIA BUEN CAFE"
        Escribir "================================"
        Escribir "1. Registrar venta"
        Escribir "2. Ver total de ventas"
        Escribir "3. Ver cantidad de ventas"
        Escribir "4. Salir"
        Escribir "Seleccione una opcion:"
        Leer opcion
		
        Si opcion = 1 Entonces
            Escribir "PRODUCTOS DISPONIBLES"
            Escribir "1. Cafe - $35.00"
            Escribir "2. Te - $25.00"
            Escribir "3. Sandwich - $50.00"
            Escribir "4. Pastel - $40.00"
            Escribir "Seleccione un producto:"
            Leer producto
			
            Si producto >= 1 Y producto <= 4 Entonces
                Segun producto Hacer
                    1:
                        nombre_producto <- "Cafe"
                    2:
                        nombre_producto <- "Te"
                    3:
                        nombre_producto <- "Sandwich"
                    4:
                        nombre_producto <- "Pastel"
                FinSegun
				
                Escribir "Producto seleccionado: ", nombre_producto
                Escribir "Ingrese la cantidad:"
                Leer cantidad
				
                Si cantidad > 0 Entonces
                    Escribir "Cantidad registrada: ", cantidad
                    Escribir "Venta capturada correctamente."
                SiNo
                    Escribir "La cantidad debe ser mayor que cero."
                FinSi
            SiNo
                Escribir "Producto no valido."
            FinSi
			
        SiNo
            Si opcion = 2 Entonces
                Escribir "Esta funcion se implementara en RF11."
            SiNo
                Si opcion = 3 Entonces
                    Escribir "Esta funcion se implementara en RF12."
                SiNo
                    Si opcion <> 4 Entonces
                        Escribir "Opcion no valida."
                    FinSi
                FinSi
            FinSi
        FinSi
    FinMientras
	
    Escribir "Programa finalizado."
FinAlgoritmo
