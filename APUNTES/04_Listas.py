## Listas ##

# Definición y caraceterísticas.

# Las listas nos permiten estructurar datos. Se pueden aplicar operaciones de reinsercción, colocación, ordenación... ya que son mutables.
# Se puede interpretar una lista como una caja, en el que cada elemento se le asocia una posición.

my_list=  list() # Una lista, almacena un array [], pero presenta operaciones no habilitadas en un []
my_other_list= []

print(len(my_list))

my_list= [24, 32, 45 , 62]

print(my_list)


my_other_list=[25, 1.7, "Giuseppe"] # Se pueden almacenar diferentes tipos de datos.

# División de elementos.

print(my_other_list[0]) #  De esta manera escogemos el primer elemento. Siempre el contaje incia en "0".
print(my_other_list[-1])#  De esta manera escogemos el último elemento. Siempre el contaje incia en "-1".
print(my_other_list[1:3]) # De esta manera escogemos un rango de elementos.

# Desempaquetado de elementos: 

age,height,name=my_other_list # A cada variable se le asocia un elemento de la lista.
print(name)

# Funciones y operaciones.

print(my_other_list.count("Giuseppe")) # La función - .count(Value) - te ofrece la cantidad de elementos semejantes en la lista.
print(my_other_list.count(25))

print(len(my_other_list)) # La función - .len(Variable) - te ofrece la cantidad de elementos que hay en una lista.

print(my_list + my_other_list) # De esta manera podemos sumar listas.
my_other_list.append(32)# La función - .append(Value) - añade un elemento a la lista al final.
print(my_other_list.append(32))

my_other_list.insert(1,"Moreno Fuentes")# La función - .insert(index, Value) - añade un elemento a la lista en una posición concreta.
print(my_other_list)

my_other_list.remove("Giuseppe")# La función - .remove(Value) - elimina un valor de la lista.
print(my_other_list) 

my_other_list.pop()# La función - .pop - elimina el último elemento por defecto.
print(my_other_list) 

del my_list[2]  # La función - del - elimina un elemento de la lista en una posición concreta.
print(my_list)

my_list.clear() # La función - .clear() - elimina todos los elementos de la lista.
print(my_list)


