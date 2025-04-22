## Funciones ## 
# Definición de una función:
# Una función, cómo su nombre lo indica, es una porción de código que se puede reutilizar en el programa.

def my_function():
    print("Hello World")
    return 0 # El return es opcional, si no se especifica se devuelve None

my_function() # Llamada a la función

def sum_two_values (a, b): # Definición de la función con dos parámetros.
    print("Suma de"+ str(a) + " y " + str(b) + " es: " + str(a+b)) # Está función suma dos valores y devulve el resultado.

sum_two_values(2, 3) # Llamada a la función con los argumentos 2 y 3. 

def sum_two_values_return (a, b): # Definición de la función con dos parámetros.
    return a + b # Está función suma dos valores y devulve el resultado.

my_value = sum_two_values_return(2, 3) # El resultado de la función se almacena en la variable my_value.

def print_name(name, surname):
    print(f"{name} {surname}") # f-string permite incluir variables dentro de una cadena de texto.

print_name("Giuseppe", "Fuentes Moreno") # Llamada a la función con los argumentos "Giuseppe" y "Fuentes Moreno".
print_name(surname="Fuentes Moreno",  name="Giuseppe") # Llamada a la función con los argumentos "Fuentes Moreno" y "Giuseppe". Los argumentos han sido cambiados de orden.

def print_name_with_default (name, surname, alias="Giu") : # Definición de la función con un parámetro opcional, qu se ejecuta de por defecto.
    print(f"{name} {surname} {alias}") 

print_name_with_default("Giuseppe", "Fuentes Moreno") # Llamada a la función con los argumentos "Giuseppe" y "Fuentes Moreno". Se ejecuta el valor por defecto de alias.


def print_texts(*text): # Definición de la función con un número indefinido de argumentos.
        print(text) # Imprime cada argumento.

print_texts("Hola", "Mundo", "Python") # Llamada a la función con los argumentos "Hola", "Mundo" y "Python", y así con todos los argumentos que se quieran añadir.



