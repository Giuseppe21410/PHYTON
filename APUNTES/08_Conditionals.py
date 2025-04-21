## Condicionales ##
# Condicionales son estructuras de control que permiten ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa.
# En Python, los condicionales se implementan con las palabras clave if, elif, if not y else.

my_condition = True 

if my_condition:
    print("La condición es verdadera.")

if my_condition == False:
    print("La condición es falsa.")# No se ejecuta porque my_condition es True.

my_condition= 2*5


if my_condition >= 10:
    print("La condición es verdadera.")# Se ejecuta porque my_condition es mayor o igual a 10.
elif my_condition < 10:
    print("La condición es falsa.")# Se ejecuta porque my_condition es menor o igual a 10. 
else:
    print("La condición es falsa.")


if my_condition == 11 or my_condition == 10:# Se ejecuta porque my_condition es 10. Con tal de una de las condiciones sea verdadera, se ejecuta el bloque de código.
    print("La condición es verdadera.")
    
if my_condition == 11 and my_condition == 10:# No se ejecuta porque my_condition es 10, y deben cumplirse ambas condiciones.
    print("La condición es verdadera.")# No se ejecuta porque my_condition es 10.
else:# Se ejecuta porque my_condition es 10.
    print("La condición no es verdadera.")

my_string = "Hola"
if my_string == "Hola":# Se ejecuta porque my_string es igual a "Hola".
    print("La cadena es igual a 'Hola'.")
    
if  not my_string:# Se ejecuta porque my_string no es una cadena vacía.
    print("La cadena no está vacía.")
else:
    print("La cadena está vacía.")
    