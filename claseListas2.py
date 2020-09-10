# import claseListas
# cant = int(input("Ingrese la cantidad de notas: "))
# notas = claseListas.cargar_teclado(cant)
# prom = claseListas.calcular_promedio(notas)
# print("Promedio es:",prom)

# n = [2, 4, 5, 10]
# n2 = n[:]
# n[1] = 10
# print(n)
# print(n2)

def read(v):
    n = len(v)
    print("Cargue los elementos del vector:")
    for i in range(n):
        v[i] = input("Casilla[" + str(i) + "]: ")

def selection_sort(v):
    # ordenamiento por seleccion directa
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] < v[j]:
                v[i], v[j] = v[j], v[i]

def linear_search(v, x):
    n = len(v)
    for i in range(n):
        if x == v[i]:
            return i
        else:
            return -1

def binary_search(v, x):
    # busqueda binaria... asume arreglo ordenado...
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1