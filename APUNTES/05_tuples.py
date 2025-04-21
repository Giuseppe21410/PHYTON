## Tuplas ##
#Definición y características:

# Las tuplas son similares a las listas, pero no se pueden modificar (son inmutables).
# Se pueden interpretar como una caja, en la que cada elemento se le asocia una posición.

my_tuple = (19, 1.76, "Giuseppe", "Fuentes Moreno") # Definición de una tupla. Se definen con paréntesis (), a diferencia del [] de las listas.
my_other_tuple = tuple(1, 2, 3, 4, 5)
my_other_tuple_1 = tuple([1, 2, 3, 4, 5]) # De esta manera se puede crear una tupla a partir de una lista, y viceversa.
#my_tuple[1]=1.77 # De esta manera no se puede modificar un elemento de la tupla, ya que es inmutable.



print(my_tuple) 

#Selección de elementos.
print(my_tuple[0]) # De esta manera escogemos el primer elemento. Siempre el contaje incia en "0".
print(my_tuple[-1]) # De esta manera escogemos el último elemento. Siempre el contaje incia en "-1".
print(my_tuple[1:3]) # De esta manera escogemos un rango de elementos.
print(my_tuple[1:]) # De esta manera escogemos todos los elementos a partir de un índice.
print(my_tuple[:3]) # De esta manera escogemos todos los elementos hasta un índice.

#Operaciones y funciones.
print(len(my_tuple)) # La función - .len(Variable) - te ofrece la cantidad de elementos que hay en una lista.
print(my_tuple.count("Giuseppe")) # La función - .count(Value) - te ofrece la cantidad de elementos semejantes en la lista.
print(my_tuple.index("Giuseppe")) # La función - .index(Value) - te ofrece la posición de un elemento en la lista.
my_sum_tuple = my_tuple + my_other_tuple # De esta manera podemos sumar tuplas.
print(my_sum_tuple)

#¿Cómo modificar una tupla?
# Para modificar una tupla, hay que convertirla a lista, modificarla y luego volver a convertirla a tupla.
my_list = list(my_tuple) # Convertimos la tupla a lista.
my_list[1] = 1.77 # Modificamos el elemento que queramos.
my_list.append("Nuevo elemento") # Añadimos un elemento a la lista.
my_list.remove("Giuseppe") # Eliminamos un elemento de la lista.
my_tuple=tuple(my_list) # Convertimos la lista a tupla.
print(my_list) # Imprimimos la lista.