"""software de promedio academico CUC"""



from Funciones_p import promedioCorte ,saludo, procesoNotas, procesoMaterias



# Presentacion
print("Bienvenido al software")

# Menú de opciones
print("Opcion 1: Promedio 30% -> Ingrese: Promedio 10% y Promedio 20%")
print("Opcion 2: Promedio 10% y 30% -> Ingrese: Notas de actividades y tareas para hallar el 10% y posteriormente hallar el 30%")
print("Opcion 3: Nota total del semestre")


# Respuesta del Usuario
op = int(input("Haz tu eleccion "))

# Condiciones
# Calcular: Promedio 30%- Caso: Promedio del 10% y del 20%
if op == 1:  
    promedio_1 = float(input("Ingresa tu nota del 10%: "))
    promedio_2 = float(input("Ingresa tu nota del 20%: "))
    if promedio_1 > 0 and promedio_2 >0:

          resultadoOp = promedioCorte(promedio_1,promedio_2)

          print(f"El resultado es: {resultadoOp}")
    else:
      print("Debes ingresar numeros positivos reales")
else:

    # Calcular: Promedio 30%- Caso: Promedio del 10% a partir de notas y el 20%

    if op == 2:
        nNotas= int(input("Cuantas notas tienes? "))
        promedio_1=procesoNotas(nNotas)
        promedio_2=float(input("Ingresa tu nota del 20%: "))
     
        if promedio_1 > 0 and promedio_2 >0:
         resultadoOp_2 = promedioCorte(promedio_1,promedio_2)

     

        else:
             print("Debes ingresar numeros positivos reales")
    else:

        if op == 3:
            
            nMaterias= int(input("Cuantas materias tienes"))
            promedioTotal=procesoMaterias(nMaterias)

            print(f"Promedio Total de tu semestre: {promedioTotal}")



        #Cuantas materias tienes, de ahi se saca la cantidad de promedios
 
        else:
            print("Error, la funcion elegida no esta dentro de las opciones del menú")