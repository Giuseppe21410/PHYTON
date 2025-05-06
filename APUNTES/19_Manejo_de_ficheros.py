## Manejo de ficheros ## 

import os # Para manejar ficheros y directorios.
import shutil # Para copiar y mover ficheros y directorios.

# Archivos .txt: 

text_file = open("APUNTES/my_file.txt", "r+") # Abre el archivo en modo lectura (r) y (w) escritura.
text_file.write("Hola, mundo!\nMe gusta el arroz.") # Escribe en el archivo.
text_file.seek(0) # Regresa al principio del archivo para leerlo desde el inicio.
print(text_file.read()) # Lee el contenido del archivo.
text_file.seek(0)
print(text_file.read(5)) # Lee los primeros 5 caracteres del archivo.
text_file.seek(0)
print(text_file.readline()) # Lee una línea del archivo.
text_file.seek(0)
print(text_file.readlines()) # Lee todas las líneas del archivo.
text_file.seek(0)
print(text_file.readlines(2)) # Lee las primeras 2 líneas del archivo.
text_file.seek(0)
for line in text_file: # Lee el archivo línea por línea.
      print(line) # Imprime cada línea del archivo.
text_file.close() # Cierra el archivo.

text_file = open("APUNTES/my_file.txt", "a") # Abre el archivo en modo añadir (a) y añade contenido al final del archivo.
text_file.write("\nHola, mundo!\nMe gusta el arroz.") # Escribe en el archivo.
text_file.close() # Cierra el archivo.

text_file = open("APUNTES/my_file.txt", "w") # Abre el archivo en modo escritura (w) y borra el contenido del archivo, ya que este modo sobreescribe el archivo.
text_file.close() # Cierra el archivo.








