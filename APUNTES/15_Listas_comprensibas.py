## Listas comprensivas ## 
# Se utilizan para crear listas de una manera más concisa y legible. 
# Se pueden usar para crear listas a partir de otras listas, aplicando operaciones o condiciones a cada elemento de la lista original. Se crean listas nuevas a partir de listas existentes, aplicando una expresión a cada elemento de la lista original.
# La sintaxis básica es: [expresión for elemento in iterable if condición].

my_original_list = [1, 2, 3, 4, 5]
my_new_list = [x**2 for x in my_original_list] # Se crea una nueva lista con los cuadrados de los elementos de la lista original
print(my_new_list) # [1, 4, 9, 16, 25]

# Se pueden aplicar condiciones para filtrar los elementos de la lista original:
my_new_list = [x**2 for x in my_original_list if x % 2 == 0] # Se crea una nueva lista con los cuadrados de los elementos pares de la lista original
print(my_new_list) # [4, 16]


my_new_list= [i + 1 for i in range(10)] # Se crea una nueva lista con los números del 1 al 10. 
# Se utiliza la función range() para generar una lista de números del 0 al 9 y se le suma 1 a cada elemento.
print(my_new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

