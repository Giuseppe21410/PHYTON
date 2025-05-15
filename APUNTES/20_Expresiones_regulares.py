## Expresiones regulares ##
# Las expresiones regulares (regex) son patrones que permiten buscar, validar y manipular texto de forma eficiente.
# Pueden ser utilizadas para buscar patrones en cadenas de texto, validar formatos.

import re 

# Exprexión match.
# La función match() busca una coincidencia en el comienzo de la cadena.
my_string="Está es la lección número 20:\n Lección llamada  Expresiones regulares."
my_other_string="Está es la lección número 19: Manejo de ficheros."


match= re.match("Está es la lección número 20",my_string, re.I)# Busca el patrón al inicio de la cadena. Si encuentra el patrón devuelve un objeto match, si no devuelve None.

print(match.group()) # Devuelve el grupo de la búsqueda.

start,end=match.span() # Devuelve la posición de inicio y fin del patrón.

print(my_string[start:end]) # Imprime el patrón encontrado.

# Expresión search.
# La función search() busca una coincidencia en cualquier parte de la cadena.

search= re.search("lección número 20",my_string, re.I) # Busca el patrón.
print(search.group()) # Devuelve el grupo de la búsqueda.

start,end=search.span() # Devuelve la posición de inicio y fin del patrón.

print(my_string[start:end]) # Imprime el patrón encontrado.

# Expresión findall.
# La función findall() busca todas las coincidencias en la cadena. 

findall=re.findall("lección",my_string, re.I) # Busca el patrón.
print(findall) # Imprime todas las coincidencias.

# Expresión split.
# La función split() divide la cadena en una lista de strings según el patrón.

split= re.split("\n",my_string)
print(split) # Imprime la lista de strings.



# Expresión sub.
# La función sub() reemplaza todas las coincidencias en la cadena.

sub=re.sub("lección", "lección 20", my_string, re.I) # Busca el patrón y lo reemplaza. Este caso es case sensitive.
print(sub) # Imprime la cadena con el patrón reemplazado.
sub=re.sub("lección|Lección","Lección 20",my_string) # Se puede también aplicar "[l|L]ección".
print (sub) # Imprime la cadena con el patrón reemplazado. Este caso es case insensitive.

# Patrones regulares.
# Los patrones regulares son expresiones que se utilizan para buscar coincidencias en una cadena de texto. 

patron= r"[lL]ección"
print(re.findall(patron,my_string)) # Busca el patrón en la cadena.

patron= r"[lL]ección|Expresiones"
print(re.findall(patron,my_string)) 

patron= r"[a-z]|[0-9]"
print(re.findall(patron,my_string))

patron=r"\d"# Busca un dígito, y no letras.
print(re.findall(patron,my_string))

patron=r"\D" # Busca un carácter no dígito.
print(re.findall(patron,my_string))

patron= r"\w" # Busca un carácter alfanumérico.
print(re.findall(patron,my_string))

patron = r"\W" # Busca un carácter no alfanumérico.
print(re.findall(patron,my_string))

patron= r"\s" # Busca un espacio en blanco.
print(re.findall(patron,my_string))

patron = r"\S" # Busca un carácter no en blanco.
print(re.findall(patron,my_string))