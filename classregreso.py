import claseListas
# Cargar por teclado un vector de N componentes y multiplicarlo por un
# valor k (ingresado por teclado).

# n = int(input("Ingrese cantidad de valores: "))
# v = []
# for i in range(n):
#     s = int(input("Ingrese un valor: "))
#     v.append(s)
#
# k = int(input("Ingrese el valor para multiplicar: "))
#
# claseListas.producto(v, k)

# print("El vector quedó:",v)
# Opción 2
n = int(input("Ingrese cantidad de valores: "))
v = n * [0]

claseListas.read(v)
k = int(input("Ingrese el valor para multiplicar: "))

claseListas.producto(v, k)

print("El vector quedó:",v)

