#Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#- NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.
 




def son_anagramas(palabra_1,palabra_2):
    if palabra_1 == palabra_2: 
        return False # Si las palabras son iguales, no son anagramas.
    return sorted(palabra_1) == sorted(palabra_2) # Comparamos las palabras y si son iguales, devuelve True. Si no, devuelve False.

while True:
    palabra_1 = input ("Escribe la primera palabra: ")
    palabra_2 = input ("Escribe la segunda palabra: ")

    palabra_1 = palabra_1.lower().replace(" ","") # Convertimos la palabra a minúsculas y eliminamos los espacios.
    palabra_2 = palabra_2.lower().replace(" ","") # Convertimos la palabra a minúsculas y eliminamos los espacios.
    
    if len(palabra_1) != len(palabra_2):
        print("Por favor, introduce palabras válidas.")
        continue # Si las palabras no tienen la misma longitud, se vuelve a pedir que introduzca las palabras.
    else: 
        for letra in palabra_1:
            if letra not in palabra_2:
                print("Por favor, introduce palabras válidas.")
                continue # Si las letras de la primera palabra no están en la segunda, se vuelve a pedir que introduzca las palabras.
    son_anagramas(palabra_1,palabra_2) # Llamamos a la función para comprobar si son anagramas.
    if son_anagramas(palabra_1,palabra_2) == True:
        print("Las palabras son anagramas.")
        break
    else:
        print("Las palabras no son anagramas.")
        continue
        

      


    


