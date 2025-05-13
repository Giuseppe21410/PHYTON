# Función que recibe un símbolo en código morse y devuelve la letra correspondiente.
def alfabeto_morse(aux):
    # Diccionario con equivalencias de morse a letras
    morse_dict = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d",
        ".": "e", "..-.": "f", "--.": "g", "....": "h",
        "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
        "--": "m", "-.": "n", "---": "o", ".--.": "p",
        "--.-": "q", ".-.": "r", "...": "s", "-": "t",
        "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
        "-.--": "y", "--..": "z", ".-.-.-": ".", "--..--": ",",
        "  ":" "
    }

    # Devuelve la letra correspondiente al código morse recibido.
    # Si no se encuentra, devuelve "?" como carácter desconocido
    return morse_dict.get(aux, "?")  


# Función que solicita al usuario una frase en morse y la traduce a texto
def morse():
    # Solicita al usuario que introduzca código morse o "/N/" para cancelar
    codigo = input("Ingresa el código morse que deseas traducir (letras separadas por espacio). Si no deseas la traducción, ingresa /N/: ")
    
    # Si el usuario ingresa "/N/", no hace nada y sale de la función
    if codigo.strip() == "/N/":
        return

    resultado = ""  # Variable donde se guardará la traducción final

    # Divide el texto morse en símbolos individuales (por cada espacio)
    letras = codigo.strip().split(" ")

    # Traduce cada símbolo usando la función alfabeto_morse()
    for simbolo in letras:
        letra = alfabeto_morse(simbolo)
        resultado += letra  # Agrega la letra al resultado

    # Muestra el texto traducido
    print("Traducción:", resultado)

          
morse()