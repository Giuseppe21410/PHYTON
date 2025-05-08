# Crea un programa que cuente cuantas veces se repite cada palabra  y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que  lo resuelvan automáticamente.


def caca ():
    string=str(input("Introduce el texto:"))
    string= string.lower()
    palabra= str(input("Introduce la palabra que deseas contar en el texto:"))
    palabra= palabra.replace(" ","")
    print(string.count(palabra))

caca()