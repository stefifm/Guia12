# cantidad = int(input("Cargue la cantidad de notas que quiera: "))
# v = []
# for i in range(cantidad):
#     nota = float(input("Ingrese una nota: "))
#     v.append(nota)
#
# print(v)

# cantidad = int(input("Cargue la cantidad de notas que quiera: "))
# v = [0] * cantidad
# for i in range(cantidad):
    #v[i] = float(input("Ingrese una nota: ")) #Se puede usar porque el v ya
    # existe aunque con el cero por la cantidad. Con el igual se reemplaza
    # los valores
#     nota = float(input("Ingrese una nota: "))
#     v.append(nota)
#
#
# print(v)

# Funciones con listas

def cargar_teclado(n):
    v = []
    for i in range(n):
        x = int(input("Cargue un valor: "))
        v.append(x)
    return v

def calcular_promedio(v):
    suma = 0
    for elemento in v:
        suma += elemento
    promedio = suma / len(v)
    return promedio

def producto(v, k):
    n = len(v)
    for i in range(n):
        v[i] *= k

def read(v):
    n = len(v)
    print("Cargue los elementos del vector: ")
    for i in range(n):
        v[i] = int(input("casilla [" + str(i) + "]: "))