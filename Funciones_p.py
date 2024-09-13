"""Funciones python"""



# Funcion para calcular el 10%

def procesoNotas(nNotas):
   
     lista = []
     suma=0
     for i in range(nNotas):
         nota= float(input(f"Ingresa tu nota numero {i+1} : "))
         lista.insert(i,nota)
         suma=suma+lista[i]
         promedioR_1= (suma/nNotas)
     return promedioR_1


# Funcion para calcular el 30%

def promedioCorte(promedio_1, promedio_2):

 resultado = ((promedio_1*0.34) + (promedio_2*0.66))
 print(resultado)
 

# Ojo faltan llos porcentajes fdel 10 y el 20 porciento

def procesoMaterias(nMaterias):
   
     lista = []
     suma=0
     promedioT=0
     nGenerica= float(input(f"Ingresa la nota de tu prueba generica: "))
     for i in range(nMaterias):
         promedioF_1= float(input(f"Ingresa tu nota numero {i+1} : "))
         promedioF_2= float(input(f"Ingresa tu nota sumativa numero {i+1} : "))
         lista.insert(i,promedioF_1+promedioF_2)
         promedioST=promedioST+lista[i]
         promedioT=((promedioST+nGenerica)/(nMaterias+1))
     return promedioT
    


def saludo():

    print("Hola mundo")