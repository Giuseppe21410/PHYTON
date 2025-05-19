#Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.

def mayuscula ():
    string=input("Ingrese la cadena de texto que quiera transformar:")
    string=string.strip().split(" ")
    print(string)
    for palabra in string:
        print(palabra.capitalize(),end=" ")

mayuscula()