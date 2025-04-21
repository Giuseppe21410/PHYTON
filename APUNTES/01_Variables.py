# Podemos declarar a las varibales diferentes tipos de datos.

variable_1= 'String'
variable_2=22.4 # -float-
variable_3=32 # -int-
variable_4= True # -bool-

print(variable_2, variable_3, variable_2) # Concanetación de  varios argumentos.
print("La edad del señor es:",variable_3) # Concaneaticón de cadenas de texto y variables.

variable_5=str(variable_3) # 'str' transforma otras clases de datos en -string-
print(variable_5, type(variable_5))

print(len(variable_1)) # 'len' Cuenta el número de caracteres dentro de la variable. Incluye los espacios.

# Variables en una sola linea: 
name, surname, age = "Giuseppe", "Fuentes Moreno",19
print ("Mi nombre es:", name, surname, "y mi edad es:",age)

# -input- Un comando que paraliza la ejecución del programa, y por la terminal te pide que se introducan datos en la variable:
nombre = input("¿Cuál es  tu nombre?:")
edad = input("Cuántos años tienes?:")

print(nombre)
print(edad)

#Cambiamos el tipo de dato a la variable:
nombre = 34
edad= "Giuseppe"

print(nombre)
print(edad)