# Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.

def fibonacci():
    print(0)
    print(1)
    aux_1= 0
    aux_2= 1
    for i in range(1,50):
        aux_3= aux_1 + aux_2
        print (aux_3)
        aux_1= aux_2
        aux_2= aux_3
   
fibonacci()

