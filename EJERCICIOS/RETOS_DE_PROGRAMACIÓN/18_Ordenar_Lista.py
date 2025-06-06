def ordenar_lista():
   lista= input("Ingrese una lista de números separados por comas: ")
   lista = lista.split(",")  # Convierte la cadena de entrada en una lista.
   print("Lista original:", lista)
   lista.sort() # Ordena la lista de menor a mayor.
   print("Lista ordenada de menor a mayor:", lista)
   lista.reverse() # Invierte el orden de la lista.
   print("Lista ordenada de mayor a menor:", lista)

ordenar_lista()