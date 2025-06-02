def vectores_ortogonales():
    v1=input("Introduce el primer vector (separado por comas): ")
    v2=input("Introduce el segundo vector (separado por comas): ")
    v1 = [int(x) for x in v1.split(",")]
    v2 = [int(x) for x in v2.split(",")]
    if len(v1) != len(v2):
        print("Los vectores deben tener la misma dimensión.")
        return
    producto_escalar = sum(x * y for x, y in zip(v1, v2)) # Calculamos el producto escalar de los vectores. Y zip combina los elementos de ambos vectores en tuplas.
    if producto_escalar == 0:
        print("Los vectores son ortogonales.")
    else:
        print("Los vectores no son ortogonales.")

vectores_ortogonales()