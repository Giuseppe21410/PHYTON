# Strings #

# Características.

my_string= "Hola"

my_new_line_string="Hola,\n¿Qué tal estas?" # Un salto de línea se representa con - \n -. 
print(my_new_line_string)
print(my_new_line_string + "\n" + my_string)

my_tab_string="\tHola" # Una tabulación se representa con - \t -.
print(my_tab_string)

my_nule_tab_string="\\tHola" # Al añadir - \\ - se anula.
print(my_nule_tab_string)

# Formateo. 

name,surname,age= "Giuseppe","Fuentes Moreno",19

print("Mi nombre es %s %s y mi edad %d." %(name,surname,age))# El mismo proceso que llevabamos a cabo en C. Utilizamos - %f - para referirnos a números tipo float.
print("Mi nombre es {} {} y tengo {}." .format(name,surname,age))
print(f"Mi nombre es {name} {surname} y tengo {age} años")# Método más éficaz denominado inferencia de datos.
print("Mi nombre es" + name + "" + surname + "y tengo" + str(age) + "años.")#Este proceso no es eficaz.

# Desempaquetado de caractéres.
language="Phyton"
a,b,c,d,e,f=language # Cda carácter del strin "Phyton" de la variable languague, se almacena en las variables correspondientes a,b,c,d,e,f.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División de caracteres. 

language_slice=language
print(language_slice[1:3])# Del primero hasta el tercero.
print(language_slice[1:])# Del primermo hasta el final.
print(language_slice[:3])# Del tercero hasta el comienzo.
print(language_slice[-2])# Se selecciona el segundo caracter contando desde el final.

# Reverse.

reversed_language=language[::-1] # Se escribe al reves.
print(reversed_language)

#Funciones. 

my_string= "Hola"
print(len(my_string)) # El comando - len() - representa la cantidad numérica de carácteres incluyendo espacios.
print(language.capitalize()) # Anidamos comandos o operaciones con - variable."comando" -. El comando - capatalize() -, pone la primera letra mayúscula.
print(language.upper())# El comando - upper() -, pone todas las letras en mayúscula.
print(language.isnumeric()) # El comando - isnumeric() - te dice si la variable es un número.
print(language.lower()) # El comando - lower() -  pone todas las letras en minúscula.
print(language.count("t"))# El comando - count() -, cuenta la cantidad de "t" presentes en la palabra.
print(language.upper().isupper())