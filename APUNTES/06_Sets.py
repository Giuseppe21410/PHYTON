## Sets # 
#Definición y características:
# - Un set es una colección desordenada de elementos únicos. No se permiten duplicados. 

my_set=set()
my_other_set={19, 1.77, "Giuseppe","Fuentes"} #Definición de un set
print(type(my_other_set))

#Operaciones y funciones:
# - No se pueden indexar, es decir, no se puede acceder a los elementos por su posición.
print(len(my_other_set)) #Longitud del set.

print("Giuseppe" in my_other_set) #Verifica si un elemento está en el set.

print("Fuentes" not in my_other_set) #Verifica si un elemento no está en el set.

my_other_set.add("Caca")#Agrega un elemento al set. Observamos que no es un conjunto ordenado, no se añade al final.

my_other_set.add("Caca") #No se agrega porque ya existe, y no se permiten duplicados.

my_other_set.remove("Caca") #Elimina un elemento del set. Si no existe, lanza un error.

print(my_other_set) #Imprime el set.

my_other_set.clear()#Limpia el set.

del my_other_set #Elimina el set.
# print(my_other_set) #Lanza un error porque el set ya no existe.

#¿ Cómo pasar un set a una lista ?
my_set = set([1,2,3,4,5])
print(my_set) #Imprime el set.
print(type(my_set)) #Imprime el tipo de dato.
my_list = list(my_set) #Convierte el set a una lista.
print(my_list[0]) #Imprime la lista, de forma indexada.
