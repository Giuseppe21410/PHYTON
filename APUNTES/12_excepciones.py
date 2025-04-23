## Excepciones ## 
# Las excepciones son errores que ocurren durante la ejecución de un programa.
# En Python, las excepciones se manejan mediante bloques try y except. Lo puedes visualizar en el diagrama de flujo. Por un error una aplicación puede dejar de funcionar, pero si se maneja correctamente, la aplicación puede continuar funcionando.

mynumber_one= 10
mynumber_two= "1"
mynumber_three= 1.5

# Por defecto, si no se maneja la excepción, el programa se detiene y muestra un mensaje de error.

try:
    print(mynumber_one + mynumber_two)
    print("No se produce ninguna excepción.") # En el momento que se produce una excepción, el programa no ejecuta esta línea.
except TypeError as e: # Se puede capturar la excepción y asignarla a una variable (e en este caso). Esto es útil para obtener más información sobre el error.
    print("Error: No se puede sumar un número y una cadena de texto.")

try:
    print(mynumber_one + mynumber_two)
    print("No se produce ninguna excepción.") 
except Exception: # Captura cualquier excepción que no sea de tipo TypeError. Esto es útil si no se sabe qué tipo de excepción puede ocurrir.
    print("Error: No se puede sumar un número y una cadena de texto.")

# En el bloque try se coloca el código que puede generar una excepción, y en el bloque except se maneja la excepción. Se pueden manejar múltiples excepciones utilizando varios bloques except.
# También se puede utilizar el bloque else para ejecutar código si no se produce ninguna excepción, y el bloque finally para ejecutar código que siempre se ejecutará, independientemente de si se produce una excepción o no.

try:
    print(mynumber_one + mynumber_three)
except TypeError: # Solo se ejecuta si se produce una excepción de tipo TypeError. Si se produce otro tipo de excepción, como un "ValueError", no se ejecuta este bloque.
    print("Error: No se puede sumar un número y una cadena de texto.")
else:
    print("La suma se realizó correctamente.")
finally:
    print("Este bloque se ejecuta siempre, independientemente de si se produce una excepción o no.")