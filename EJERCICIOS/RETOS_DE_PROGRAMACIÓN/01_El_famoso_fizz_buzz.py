#Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

number = 0
print("Ejercicio 1: FizzBuzz")
number= int(input("Escribe un número: "))
 
def if_fizz_buzz(number):
     if number < 1 or number > 100:
         print("El número no está en el rango de 1 a 100.Vueleve a ingresar un número.")
         number = int(input("Escribe un número: "))
         if number < 0 or number > 100:
             if_fizz_buzz(number) 
                   
if_fizz_buzz(number)



def fizz(number):
   for i in range(number,101):
    if i % 3 == 0:
     print(i)
     print("\n")

def buzz(number):
   for i in range(number,101):
    if i % 5 == 0:
     print(i)
     print("\n")

def fizz_buzz(number):
   for i in range(number,101):
    if i % 5 == 0 and i % 3 == 0:
     print(i)
     print("\n")


print("Estás son las opciones posibles:")
print("1. Fizz")
print("2. Buzz")
print("3. FizzBuzz")

opcion = int(input("Selecciona una opción: "))
if opcion == 1:
    fizz(number)
elif opcion == 2:
    buzz(number)
elif opcion == 3:
    fizz_buzz(number)
else:
  print("Opción no válida. Por favor, selecciona una opción válida.")
  opcion = int(input("Selecciona una opción: "))
