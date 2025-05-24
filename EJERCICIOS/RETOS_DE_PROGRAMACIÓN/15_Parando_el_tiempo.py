
import time

def parando_el_tiempo ():
    numero_1= int(input("ingrese el primer numero: "))
    numero_2=int(input("Ingresa el segundo número:"))
    segundos=input("Ingrese el tiempo en segundos:")
    time.sleep(segundos) # Espera 4 segundos a enviar el resultado del mensaje.
    print(f"El resultado de la suma de {numero_1} + {numero_2} . Tiempo de espera: {segundos} segundos")

parando_el_tiempo()
