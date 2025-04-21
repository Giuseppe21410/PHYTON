## Bucles ## 
# Definicion:
# Un bucle es una estructura de control que permite ejecutar un bloque de codigo varias veces.
# Existen dos tipos de bucles en Python: el bucle for y el bucle while.

# El bucle while se utiliza para ejecutar un bloque de codigo mientras una condicion sea verdadera.
# La sintaxis del bucle while es la siguiente:

my_condition=0

while my_condition < 5:
    print(my_condition) # Imprime el valor de my_condition en cada iteracion del bucle
    my_condition += 1 # Incrementa el valor de my_condition en 1 en cada iteracion del bucle
else:
    print("El bucle while ha terminado") # El bloque else se ejecuta una vez que la condicion del bucle while ya no es verdadera.

while my_condition < 10:
    print(my_condition) # Imprime el valor de my_condition en cada iteracion del bucle
    my_condition += 1 # Incrementa el valor de my_condition en 1 en cada iteracion del bucle
    if my_condition == 7:
        break # El bucle se interrumpe cuando my_condition es igual a 7.

# El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o un string) o sobre un rango de numeros.
# La sintaxis del bucle for es la siguiente:

my_list = [1, 2, 3, 4, 5] # Definimos una lista de numeros

for number in my_list: # Iteramos sobre cada elemento de la lista
    print(number) # Imprime cada numero de la lista

for letter in "Python": # Iteramos sobre cada letra de la cadena "Python"
    print(letter) # Imprime cada letra de la cadena

for element in range(10): # Iteramos sobre un rango de numeros del 0 al 9
    print(element) # Imprime cada numero del rango

for element in range(5, 10): # Iteramos sobre un rango de numeros del 5 al 9
    print(element) # Imprime cada numero del rango

for element in range(5, 10, 2): # Iteramos sobre un rango de numeros del 5 al 9 con un paso de 2
    print(element) # Imprime cada numero del rango

for element in my_list: # Iteramos sobre cada elemento de la lista
    if element == 3: # Si el elemento es igual a 3
        continue # Se salta a la siguiente iteracion del bucle
    print(element) # Imprime cada numero de la lista excepto el 3

for element in my_list: # Iteramos sobre cada elemento de la lista
    if element == 3: # Si el elemento es igual a 3
        break # El bucle se interrumpe cuando se encuentra el 3
    print(element) # Imprime cada numero de la lista excepto el 3

# El diccionario es una estructura no iterable, por lo que no se puede utilizar un bucle for para iterar sobre sus elementos.
# Sin embargo, se puede utilizar un bucle for para iterar sobre las claves o los valores del diccionario.


my_dict = {"nombre": "Giuseppe", "edad": 25, "altura": 1.77} # Definimos un diccionario con tres claves y sus respectivos valores

for element in my_dict: # Iteramos sobre las claves del diccionario
    print(element) # Imprime cada clave del diccionario

for element in my_dict.values(): # Iteramos sobre los valores del diccionario
    print(element) # Imprime cada valor del diccionario

