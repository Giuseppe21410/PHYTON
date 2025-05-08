# Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
#- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def caca():
    cadena_de_texto = str(input("Introduce una cadena de texto: "))
    longitud = len(cadena_de_texto)
    for letra in range(longitud -1,-1,-1):
        print(cadena_de_texto[letra], end="")
        
    
caca()