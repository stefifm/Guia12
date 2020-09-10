import claseListas2

def test():
    n = int(input("Cantidad de elementos: "))
    v = n * [0]
    claseListas2.read(v)
    x = input("Valor a buscar: ")
    ind = claseListas2.binary_search(v, x)
    if ind >= 0:
        print("Está en la casilla:", ind)
    else:
        print("No está en el arreglo")

if __name__ == '__main__':
    test()
