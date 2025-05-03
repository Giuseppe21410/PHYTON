## Funciones de orden superior ##
# Las funciones de orden superior son funciones que pueden recibir otras funciones como argumentos o devolver funciones como resultado. Estas funciones son útiles para crear funciones más complejas y reutilizables.

def sum_one(value):
    return value + 1 # Definimos una función que suma 1 a un valor.

def sum_two_values(x, y):
    return sum_one(x + y) # Definimos una función que suma dos valores y luego aplica la función sum_one al resultado. 

print(sum_two_values(5, 10)) # Imprimimos el resultado de la función que suma dos valores y aplica la función sum_one al resultado.

# Otro ejemplo de función de orden superior consiste en una función que recibe otra función como argumento. 

def sum_one(value):
    return value + 1 

def sum_two_values(x, y, func):
    return func(x + y) # Definimos una función que suma dos valores y luego aplica la función func al resultado.

print(sum_two_values(5, 10, sum_one))

## Clousure ##
# Una función de orden superior que devuelve otra función. La función devuelta puede acceder a las variables de la función que la creó, incluso después de que la función original haya terminado su ejecución.

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value # Definimos una función que suma 10 a un valor y al valor original que se pasó a la función sum_ten.
    return add # Devolvemos la función sum_ten.
add_clousure = sum_ten(5) # Llamamos a la función sum_ten con el valor 5 y guardamos la función devuelta en add_clousure.
## La función add_clousure ahora es una función que suma 10 al valor que se le pase como argumento, además de sumar el valor original que se pasó a la función sum_ten.
print(add_clousure(5)) 
print(sum_ten(5)(1)) # Llamamos a la función sum_ten con el valor 5 y luego llamamos a la función devuelta con el valor 5.


## Funciones de orden superior construidas. ##

# La función map().
# La función map() se utiliza para aplicar una función a cada elemento de una lista o iterable. La función map devuelve un objeto iterable, por lo que se debe convertir a una lista para imprimirlo. 



numbers = [1, 2, 9, 14, 32] # Definimos una lista de números.

def multiply_by_two(value):
    return value * 2 # Definimos una función que multiplica un valor por 2.

print(list(map(multiply_by_two, numbers))) # Usamos la función map para aplicar la función multiply_by_two a cada elemento de la lista numbers. La función map devuelve un objeto iterable, por lo que lo convertimos a una lista para imprimirlo.

print(list(map(lambda x: x + 1, numbers))) # Usamos la función map para aplicar una función lambda que suma 1 a cada elemento de la lista numbers. La función map devuelve un objeto iterable, por lo que lo convertimos a una lista para imprimirlo.

# La función filter()
# La función filter() se utiliza para filtrar elementos de una lista o iterable según una función que devuelve True o False. La función filter devuelve un objeto iterable, por lo que se debe convertir a una lista para imprimirlo.

def filter_greater_than_ten(value):
    if value > 10: # Definimos una función que devuelve True si el valor es mayor que 10.
        return True
    else:
        return False # De lo contrario, devuelve False.

print(list(filter(filter_greater_than_ten, numbers))) # Usamos la función filter para aplicar la función filter_greater_than_ten a cada elemento de la lista numbers. La función filter devuelve un objeto iterable, por lo que lo convertimos a una lista para imprimirlo.
print(list(filter(lambda x: x > 10, numbers))) # Usamos la función filter para aplicar una función lambda que devuelve True si el valor es mayor que 10. La función filter devuelve un objeto iterable, por lo que lo convertimos a una lista para imprimirlo.

# La función reduce().
# La función reduce() se utiliza para aplicar una función a los elementos de una lista o iterable de manera acumulativa. La función reduce devuelve un solo valor, por lo que no es necesario convertirlo a una lista.
from functools import reduce # Importamos la función reduce del módulo functools.

def sum_two_values(x, y):
    print(x)
    print(y)
    return x + y # Definimos una función que suma dos valores.

print(reduce(sum_two_values, numbers)) # Usamos la función reduce para aplicar la función sum_two_values a los elementos de la lista numbers de manera acumulativa. La función reduce devuelve un solo valor, por lo que no es necesario convertirlo a una lista.
print(reduce(lambda x, y: x + y, numbers)) # Usamos la función reduce para aplicar una función lambda que suma dos valores. La función reduce devuelve un solo valor, por lo que no es necesario convertirlo a una lista.

