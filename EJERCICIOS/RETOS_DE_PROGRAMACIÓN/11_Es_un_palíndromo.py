
def palindromo():
    cadena_de_texto= input("Introduce la frase que quieras verificar como un palíndromo:")
    cadena_de_texto= cadena_de_texto.lower().replace(" ","")

    if cadena_de_texto==cadena_de_texto[::-1]:
        print("Es un políndromo.")
    else:
        print("No es un políndromo.")
    

palindromo()