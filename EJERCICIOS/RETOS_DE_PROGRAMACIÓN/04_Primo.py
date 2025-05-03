# Escribe un programa que se encargue de comprobar si un número es o no primo.  Hecho esto, imprime los números primos entre 1 y 100.

def es_primo(número):
    for i in range(2, número -1): 
        if número % i == 0: # Si el número es divisible por i, no es primo.
            return False
    return True # Si no se encuentra ningún divisor, el número es primo.


while True:
    número = int(input("Escribe un número: "))
    if número <=0: 
        print("El número no es válido. Por favor, introduce un número mayor que 0.")
        continue
    es_primo(número) # Llamamos a la función para comprobar si es primo.
    if es_primo(número) == True:
        print("El número es primo.")
        print(" Estos son todos los números primos que hay desde 1 hasta el 50:")
        for i in range(1, 51): 
            if es_primo(i) == True: # Si el número es primo, lo imprimimos.
                print(i, end=", ") # Imprimimos los números primos entre 1 y 50 en la misma línea.
        print("\n")
        break
    else:
        print("El número no es primo.")
        continue
