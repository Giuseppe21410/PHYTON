# Aquí se muestran el conjunto de operadores: 
# Operadores básicos:
print (2-3)
print (1/4)
print (2*3)
print (3+4)
print (10%2) # - % - El operador de módulo te da el resto de la división.
print (10//3) # - // - El operador hace una división que no incluye los elementos décimales, al aproximarse a un número entero.
print (2**3) # . ** - El operador representa las potencias.

# Operadores con otros tipos de datos: 
print ("Hola" + " Soy Giuseppe") # Se combinan en una sola cadena de texto dos cadenas de texto.
print ("Hola " + str(5)) # De esta manera combinamos diferentes tipos de datos.
print ("Hola "  *  5) # Se representa 5 veces "Hola".
my_float=2.5
print ("Adiós " * int(2.5 *2)) # Transformamos el tipo "float" a " integer".

# Operadores de comparación: 

print (3<4)
print (3>4)
print (3>=4)
print (3<=4)
print (3==4) # - == - ¿Es igual qué...? 
print ( 3 != 4) # - != - ¿Es distinto que...?
print (3 > 4 == 2) # Se pueden anidar operadores.
print ( "Hola" < "Phyton") # Se comparan cadenas de texto en función de su ordenación alfabética.
print (len("Hola") > len( "Phyton")) # Se comparan cadenas de texto en función de la cantidad de carácteres.
print ("Hola" < "Bola")
print ("Hola" > "Zola")

# Operadores lógicos: 
print ( 3 > 4 and "Hola"> "Phyton" )
print (3 < 4 or "Hola"> "Phyton")
print ( 3<4 or ("Hola" > "Phyton" and 4==4))
print (not(3>4))