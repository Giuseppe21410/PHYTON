## Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

def factorial(): 
    numero= int(input("Ingrese el número que quiera cálcular: "))
    numero_2=1
    numero_3=numero

    for numero_1 in range(numero,0,-1):
        if numero_1==1: 
            print(f"\nEl factorial de {numero_3} es: {numero_2}")
            return
        numero_2*=numero_1
        print(numero_2,end=" ")
        
        
factorial()