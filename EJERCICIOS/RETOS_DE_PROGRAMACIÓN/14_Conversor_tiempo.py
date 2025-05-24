## Crea una función que reciba días, horas, minutos y segundos (como enteros)  y retorne su resultado en milisegundos.

def conversor ():
    dia=int(input("Indique los días:"))
    hora=int(input("Indique las horas:"))
    segundo=int(input("indique los segundos:"))

    milisegundos= dia*86400000 + hora*3600000 + segundo*1000
    print(f"El número de milisegundos es:{milisegundos} milisegundos.")

conversor()