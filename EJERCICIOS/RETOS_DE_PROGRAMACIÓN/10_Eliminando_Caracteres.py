
def eliminado_caracteres():
    str_1=input("Introduce la primera cadena de texto:")
    print("\n")
    str_2=input("Introduce la segunda cadena de texto:")


    for letra in str_1:
        for letra_1 in str_2:
            if letra==letra_1:
                str_2=str_2.replace(letra_1,"")
                str_1=str_1.replace(letra,"")
                break
            if letra!=letra_1:
                str_2=str_2.replace(letra_1,"")
                break
    
    print(f"Los caracteres presentes en la primera cadena de texto, pero presentes en la segunda cadena de texto son:{str_1}")

    str_1=input("Introduce la primera cadena de texto:")
    print("\n")
    str_2=input("Introduce la segunda cadena de texto:")

    for letra in str_2:
        for letra_1 in str_1:
            if letra==letra_1:
                str_2=str_2.replace(letra,"")
                str_1=str_1.replace(letra_1,"")
                break
            if letra!=letra_1:
                str_1=str_1.replace(letra_1,"")
                break
    print(f"Los caracteres presentes en la segunda cadena de texto, pero no  presentes en la primera cadena de texto son:{str_2}")



eliminado_caracteres()