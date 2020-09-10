# 1. Pluviómetro
# Se ha solicitado un programa que permita cargar las precipitaciones
# promedio en cada mes del país, en base a esos datos armar un menú de
# opciones que permita:
#
# Determinar el promedio anual de lluvias
# Determinar el promedio de lluvias para un determinado trimestre
# Determinar el mes más seco del año
# Determinar los meses del año en los que llovió más que el promedios de
# lluvia de todo el año.

import random

# Funciones

# def cargar_vector(lluvias):
#     n = len(lluvias)
#     for i in range(n):
#         lluvias[i] = random.uniform(45.8, 160.1)
#     return lluvias

def promedio(vec):
    suma = 0
    cant = len(vec)
    promedio = 0
    for i in range(len(vec)):
        suma += vec[i]
    if cant != 0:
        promedio = suma / cant
    return promedio

def validar_rango(mensaje="Ingrese un valor: "):
    num = 0
    while num < 1 or num > 4:
        num = int(input(mensaje))
        if num < 1 or num > 4:
            print("Error. Elija un número entre 1 y 4.")
    return num

def rango_trimestre(trimestre):
    if trimestre == 1:
        return range(3)
    elif trimestre == 2:
        return range(3, 6)
    elif trimestre == 3:
        return range(6, 9)
    else:
        return range(9, 12)

def promedio_trimestre(lluvias):
    trimestre = validar_rango("Ingrese el trimestre para calcular: ")
    suma = 0
    rango = rango_trimestre(trimestre)
    for i in rango:
        suma += lluvias[i]
    promedio = suma / len(rango)
    return trimestre, promedio


def mes_seco(lluvias):
    menor = ()
    tam = len(lluvias)

    for m in range(tam):
        if m == 0:
            menor = m, lluvias[m]
        else:
            if menor[1] > lluvias[m]:
                menor = m, lluvias[m]
    return menor[0]




def meses_mas_prom(lluvias, prom):
    vec_aux = []
    for i in range(len(lluvias)):
        if lluvias[i] > prom:
            vec_aux.append(lluvias[i])
    return vec_aux
# Funcion principal

def test():
   menu = "Menú de opciones\n"\
          "1- Cálculo del promedio anual de llluvias\n"\
          "2- Cálculo del promedio de lluvias por trimestre\n"\
          "3- Mes más seco del año\n"\
          "4- Meses cuyas cantidades de lluvias superaron al promedio\n"\
          "5- Salir\n"\
          "Elija una opcion: "
   opcion = -1

   # Cargar vector de lluvias
   n = int(input("Ingrese la cantidad de meses: "))
   vec_lluvia = n * [0]
   for i in range(len(vec_lluvia)):
       vec_lluvia[i] = random.randint(45, 160)

   while opcion != 5:
       opcion = int(input(menu))
       prom = 0
       if opcion == 1:
           prom_anual = promedio(vec_lluvia)
           print("Promedio anual de lluvias:",prom_anual,"mm")
       elif opcion == 2:
           trimestre = promedio_trimestre(vec_lluvia)
           print("El promedio de lluvias del trimestre",trimestre[0],
                 "fue de",trimestre[1],"mm")
       elif opcion == 3:
           mes_mas_seco = mes_seco(vec_lluvia)
           print("El mes con menos lluvia:",mes_mas_seco + 1)
       elif opcion == 4:
           prom = promedio(vec_lluvia)
           mas_prom = meses_mas_prom(vec_lluvia,prom)
           print("Meses que superan el promedio anual de lluvia:",mas_prom)

if __name__ == "__main__":
    test()
