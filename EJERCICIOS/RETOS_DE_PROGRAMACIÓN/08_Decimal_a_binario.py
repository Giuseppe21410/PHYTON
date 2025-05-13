#Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


def binario():
    num= int(input("Ingresa el número que quieras traducir a binario:"))
    
    if num==0:
        print("0")
        return
    resultado=""
    while num > 0: 
        residuo = num % 2 
        resultado = str(residuo) + resultado
        num= num // 2 
   
    longitud= len(resultado)
    print("Binario:",end=" ")
    for letra in range(longitud -1,-1,-1):
        print(resultado[letra],end="" )

binario()

    
