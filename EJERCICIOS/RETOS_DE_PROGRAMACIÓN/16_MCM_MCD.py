def mcm_mcd():
    num_1= int(input("Introduce el primer número: "))
    num_2= int(input("Introduce el segundo número: "))
    lista=[]

    for i in range(1, num_1):
        for i in range(1, num_2):
            if num_1 % i == 0 and num_2 % i == 0:
                lista.append(i)
            
    mcd = max(lista) # Máximo común divisor (MCD)      
    mcm = (num_1 * num_2) / mcd # Calculo del mínimo común múltiplo (MCM)

    print(f"El MCD de {num_1} y {num_2} es: {mcd}")
    print(f"El MCM de {num_1} y {num_2} es: {mcm}")
       
mcm_mcd()
        
            
         

