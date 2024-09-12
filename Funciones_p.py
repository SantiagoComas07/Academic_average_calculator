"""Funciones python"""




# Declaracion de variables

#def PeticionNotas(notaUno, notaDos, notaTres, notaCuatro, notaSumativa):

#promedio_1= (notaUno+notaDos+notaTres+notaCuatro)*(0.10)
#promedio_2= (notaSumativa)*(0.20)
#Resultado=  (promedio_1+promedio_2)
#return Resultado

def procesoNotas(nNotas):
   
     lista = []
     suma=0
     promedio_1=0
     for i in range(nNotas):
         nota= float(input(f"Ingresa tu nota numero {i+1} : "))
         lista.insert(i,nota)
         suma=suma+lista[i]
         promedioR_1= suma/nNotas


# def promedioGeneral(promedio_1, notaSumativa)

#     total= promedio_1 + notaSumativa



def promedioCorte(promedio_1, promedio_2):

    resultado = (promedio_1 + promedio_2)/2
    print(resultado)
 
def saludo():

    print("Hola mundo")