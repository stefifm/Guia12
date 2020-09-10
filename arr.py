print("Arreglos con primos")

import random

def validar(inf):
    n = inf
    while n <= inf:
        n = int(input("Carhue la cantidad de elementos del arreglo: "))
        if n <= inf:
            print("Error. La cantidad de elementos no debe ser menor o igual a cero.")
    return n

def cargar_vector(v):
    n = len(v)
    for i in range(n):
        v[i] = random.randint(1, 100)
    return v

def vector_primos(v):
    n = len(v)
    v_p = []
    for i in range(n):
        if v[i] % 2 != 0:
            v_p.append(v[i])
    return v_p

def promedio(v_p):
    suma = 0
    prom = 0
    n = len(v_p)
    for i in range(n):
        suma += v_p[i]
    if n != 0:
        prom = round(suma / n, 2)
    return prom

#Funcion principal

def test():
    #Validar N
    n = validar(0)
    #Carga del vector
    v = n * [0]
    cargar_vector(v)
    #Vector de primos
    vec_primos = vector_primos(v)
    #Promedio del vector primo
    prom_primos = promedio(vec_primos)
    #Resultados
    print("Vector normal:",v)
    print("Vector de números primos:",vec_primos)
    print("Promedio de números primos:",prom_primos)





if __name__ == "__main__":
    test()