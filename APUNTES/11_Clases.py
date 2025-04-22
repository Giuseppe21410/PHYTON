## Clases ##
# Definición:
# Una clase es un molde para crear objetos. Un objeto es una instancia de una clase. Identifican objetos dentro de un ámbito de actuación.

class EmptyPerson: # Definición de la clase. Es costumbre escribir el nombre de la clase con mayúscula, sin espacios ni guiones bajos.
    pass # Evita la clase.

class Person: 
    def __init__(self, name , surname): # Un constructor es un método especial que se ejecuta al crear un objeto de la clase. Se define con el nombre __init__ y siempre recibe como primer parámetro self, que es una referencia al objeto que se está creando.
        self.name = name # self.name es un atributo de la clase. Se puede acceder a él desde fuera de la clase con el nombre del objeto seguido de un punto y el nombre del atributo.
        self.surname = surname 
    
my_persona = Person("Giuseppe" , "Fuentes Moreno") #Se almacena 

print(my_persona.name) # Se accede a los atributos de la clase con el nombre del objeto seguido de un punto y el nombre del atributo.

class Person1:
    def __init__(self, name, surname, alias="Sin alias por defecto"): # Se puede definir un valor por defecto para un parámetro. En este caso, el parámetro alas tiene un valor por defecto de "Sin alias por defecto.".
        self.full_name= f"{name} {surname} {alias}" # Se puede crear un atributo a partir de otros atributos. En este caso, se crea el atributo full_name a partir de los atributos name y surname.
    def walk(self):
        print(f"{self.full_name} Camina")

my_persona1 = Person1("Giuseppe", "Fuentes Moreno") # Se crea un objeto de la clase Person1.

print(my_persona1.full_name) # Se accede al atributo full_name del objeto my_persona1.

my_persona1.walk() # Se llama a la función walk del objeto my_persona1. La función walk imprime un mensaje que incluye el nombre completo de la persona.

my_other_persona = Person1("Giuseppe", "Fuentes Moreno", "Giu") # Se crea otro objeto de la clase Person1 con un alias.

print(my_other_persona.full_name) # Se accede al atributo full_name del objeto my_other_persona.

my_other_persona.full_name= "Giusepe Fuentes Moreno Giuse" # Se puede modificar el valor de un atributo de un objeto. El constructor de una clase no es inmutable, se puede modificar el valor de los atributos de un objeto después de haberlo creado.