"""software de promedio academico CUC"""



from Funciones_p import promedioCorte ,saludo, procesoNotas




# Presentacion
print("Bienvenido al software")

# Menú de opciones
print("Opcion 1: Promedio 30% -> Ingrese: Promedio 10% y Promedio 20%")
print("Opcion 2: Promedio 10% -> Ingrese: Notas de actividades y tareas")
print("Opcion 3: Nota total del semestre")


# Respuesta
op = int(input("Haz tu eleccion "))

# Condiciones
# Promedios completos
if op == 1:  
    promedio_1 = float(input("Ingresa tu nota del 10%: "))
    promedio_2 = float(input("Ingresa tu nota del 20%: "))
    if promedio_1 > 0 and promedio_2 >0:

          resultadoOp = promedioCorte(promedio_1,promedio_2)

          print(f"El resultado es: {resultadoOp}")
    else:
      print("Debes ingresar numeros positivos reales")
else:
    if op == 2:
        nNotas= int(input("Cuantes notas tienes? "))
        promedio_1=procesoNotas(nNotas)
        promedio_2=float(input("Ingresa tu nota del 20%: "))
     
        # print(type(promedio_1))

        # Problema 
        # if promedio_1 is None:
        #     valorFloat=0.0
        # else:
        #      valorFloat=float(promedio_1)

        if promedio_1 > 0 and promedio_2 >0:
         resultadoOp_2 = promedioCorte(promedio_1,promedio_2)
        else:
             print("Debes ingresar numeros positivos reales")
    else:


        # saludo()
    # notaUno = float(input("Ingresa tu primera nota"))
    # notaDos = float(input("Ingresa tu primera nota"))
    # notaTres = float(input("Ingresa tu primera nota"))
    # notaCuatro = float(input("Ingresa tu primera nota"))

    # nNotas = int(input("Ingresa el numero de notas"))

    # notasm = procesoNotas(nNotas)

    # print(f"{notasm}")

    # Nota Sumativa
    # notaSumativa = float(input("Sumativa"))

    # print(f"{promedioGeneral(promedio_1, notaSumativa)}")
        if op == 3:
            print("Hola")


        #Cuantas materias tienes, de ahi se saca la cantidad de promedios
 
        else:
            print("Error, la funcion elegida no esta dentro de las opciones del menú")


