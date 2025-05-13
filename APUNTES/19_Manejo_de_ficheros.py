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

# os.remove("APUNTES/my_file.txt")  Elimina el archivo.


## Archivos .json:

import json

json_file = open("APUNTES/my_file.json", "w")

json_test= { # Los archivos .json, almacenan objetos de mapeo como los diccionarios.
      "name":"Giuseppe",
      "surname":"Fuentes Moreno",
      "age":20,
      "language":"Phyton"}

json.dump(json_test,json_file,indent=1) # Abre un fichero con el contenido de json_test.

json_file.close()

with open("APUNTES/my_file.json") as my_other_file: # Abre el archivo con un nombre, y lee linea por linea el contenido.
      for line in my_other_file:
       print(line)


json_dict =json.load(open("APUNTES/my_file.json")) # Carga el contenido del archivo en un diccionario.
print(json_dict)

# Archivos CSV: 

import csv

csv_file = open("Apuntes/my_file.csv", "w+") #Creamos un archivo y lo inicializamos en una variable.

csv_writer= csv.writer(csv_file) # Inicializamos una variable que escriba el documento.

csv_writer.writerow(["Name","Surname","Occupation"]) #Crea un row con tres columnas.
csv_writer.writerow(["Giuseppe","Fuentes Moreno","Student"])





