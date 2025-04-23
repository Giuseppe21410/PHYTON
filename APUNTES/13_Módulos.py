## Módulos ##
# Un módulo es un archivo que contiene definiciones y declaraciones de Python. Este puede definir funciones, clases y variables. Un módulo puede incluir código ejecutable.
# A la hora de importar un módulo, no se acepta una nomencltura de números al comienzo. Se debe usar un nombre que empiece por letra y que no contenga espacios ni caracteres especiales.

import modules # Importa el módulo completo

modules.sum(2, 3) # Llama a la función sum del módulo modules
modules.printHelloWorld() # Llama a la función printHelloWorld del módulo modules

# Se pueden importar módulos de la siguiente manera:
from modules import sum # Importa solo la función sum del módulo modules
from modules import printHelloWorld # Importa solo la función printHelloWorld del módulo modules

sum(2, 3) # Llama a la función sum del módulo modules
printHelloWorld() # Llama a la función printHelloWorld del módulo modules

from modules import * # Importa todas las funciones del módulo modules
