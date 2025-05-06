
def menu(): 
    print("¿Cuál es la base del polígono?")
    base = float(input("Base: "))
    print("¿Cuál es la altura del polígono?")
    altura = float(input("Altura: "))
    
    while True:
        print("Elige uno de los siguientes polígonos para calcular su área:")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        opcion = int(input("Opción: "))
        if opcion in [1, 2, 3] and base > 0 and altura > 0:
            return opcion, base, altura
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            continue
   
    

def polígono (opcion, base, altura):
    if opcion == 1 and base==altura: 
        area= base**2
        print(f"El área del cuadrado es: {area}")
    elif opcion == 2:
        area= base*altura
        print(f"El área del rectángulo es: {area}")
    elif opcion == 3:
        area= (base*altura)/2
        print(f"El área del triángulo es: {area}")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
        menu()
    

opcion, base, altura = menu() # Llamamos a la función menu y guardamos los valores en las variables opcion, base y altura.
polígono(base, altura, opcion) 


    