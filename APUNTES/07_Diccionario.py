## Diccionarios ##
# Definición:
# Un diccionario es una colección de pares clave-valor.Se definen con llaves {} y los pares clave-valor se separan por comas.

my_dict = dict()
print(type(my_dict)) # <class 'dict'>

my_dict = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
}# Se puede crear un diccionario vacío con dict() o con {}. A cada elemento se le asigna una clave y un valor.

my_other_dict = {
    'nombre': 'Pedro',
    'edad': 25,
    'ciudad': 'Barcelona',
    'lenguajes': {'Phyton', 'Java', 'C+++', 'JavaScript' },#Se puede almacenar listas, sets o tuplas dentro de un diccionario.
}

print(my_other_dict)

print(my_other_dict['lenguajes']) #  {'Phyton', 'Java', 'C+++', 'JavaScript' }

print(len(my_other_dict)) # En este caso, el resultado es 4 porque hay 4 pares clave-valor en el diccionario.


my_other_dict['nombre'] = 'Juan' # Cambia el valor de la clave 'nombre' a 'Juan'

my_other_dict['pais'] = 'España' # Agrega un nuevo par clave-valor al diccionario.
print(my_other_dict) 
 
del my_other_dict['pais'] # Elimina el par clave-valor con la clave 'pais'.

# Operaciones:

print("nombre" in my_other_dict) # True, porque 'nombre' es una clave en el diccionario. Solo considera las claves, no los valores.

print(my_other_dict.clear()) # Elimina todos los pares clave-valor del diccionario.

print(my_dict.items()) # Devuelve una vista de los pares clave-valor del diccionario.

print(my_dict.keys()) # Devuelve una vista de las claves del diccionario.

print(my_dict.values()) # Devuelve una vista de los valores del diccionario.

print(my_dict.get('nombre')) # Devuelve el valor asociado a la clave 'nombre'. Si la clave no existe, devuelve None.

print(my_other_dict.fromkeys("Nombre",1)) # Crea un nuevo diccionario con las claves de la cadena "Nombre" y el valor 1 para cada clave. El resultado es {'N': 1, 'o': 1, 'm': 1, 'b': 1, 'r': 1} porque cada letra de la cadena se convierte en una clave del nuevo diccionario.
print(my_other_dict.fromkeys(["Nombre", "Apellido"], 1)) # Crea un nuevo diccionario con las claves de la lista ["Nombre", "Apellido"] y el valor 1 para cada clave. El resultado es {'Nombre': 1, 'Apellido': 1} porque cada elemento de la lista se convierte en una clave del nuevo diccionario.
print(my_other_dict.fromkeys(["Nombre", "Apellido"], [1, 2])) # Crea un nuevo diccionario con las claves de la lista ["Nombre", "Apellido"] y el valor [1, 2] para cada clave. El resultado es {'Nombre': [1, 2], 'Apellido': [1, 2]} porque cada elemento de la lista se convierte en una clave del nuevo diccionario y el valor es la lista completa.
print(my_other_dict.fromkeys(["Nombre", "Apellido"]))# Crea un nuevo diccionario con las claves de la lista ["Nombre", "Apellido"] y el valor {None} para cada clave. El resultado es {'Nombre': {1, 2}, 'Apellido': {1, 2}} porque cada elemento de la lista se convierte en una clave del nuevo diccionario y el valor es el conjunto completo.

print(list(my_other_dict.items())) # Convierte los pares clave-valor del diccionario en una lista de tuplas. Cada tupla contiene un par clave-valor.
print(list(my_other_dict.keys())) # Convierte las claves del diccionario en una lista.
print(list(my_other_dict.values())) # Convierte los valores del diccionario en una lista.
# Lo mismo para las tuplas y sets.
print(tuple(my_other_dict.items())) # Convierte los pares clave-valor del diccionario en una lista de tuplas. Cada tupla contiene un par clave-valor.
print(set(my_other_dict.items())) # Convierte los pares clave-valor del diccionario en una lista de tuplas. Cada tupla contiene un par clave-valor.