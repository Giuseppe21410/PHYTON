## Fechas ##
# Las fechas son objetos de la clase datetime.  

from datetime import datetime

now = datetime.now() # Inicializamos un objeto de tipo "datetime", función que está dentro del módulo datetime.

#Visualuzación de la fecha actual:
print(now) # Imprimimos la fecha actual en formato datetime.

timestap = now.timestamp()

print(timestap) # Nos da la fecha en segundos desde el 1 de enero de 1970.

print(datetime.fromtimestamp(timestap)) # Nos da la fecha en formato datetime.

print(now.day) # Nos da el día y así sucesivamente.
print(now.hour) 
print(now.minute)
print(now.month)



# Veamos cómo se puede establecer una  fecha:
# Para ello, se utiliza la función datetime() de la clase datetime.
# Esta función recibe como parámetros el año, mes, día, hora, minuto y segundo.

def print_date(date):
    print(now.day) 
    print(now.hour)  
    print(now.minute)
    print(now.month)
    
print_date(now) # Imprimimos la fecha actual.

year_2023= datetime(2023, 1, 1, 0, 0, 0) # Inicializamos un objeto de tipo "datetime" con la fecha 1 de enero de 2023 a las 00:00:00.
 
print_date(year_2023) # Imprimimos la fecha 1 de enero de 2023.

# Vemos la clase time:
# La clase time es una subclase de la clase datetime.
# Esta clase se utiliza para representar una hora en el día, sin fecha.

from datetime import time

current_time = time(12, 30, 0) # Inicializamos un objeto de tipo "time" con la hora 12:30:00.

print(current_time) # Imprimimos la hora 12:30:00.

print(current_time.hour) # Imprimimos la hora.
print(current_time.minute) # Imprimimos los minutos.
print(current_time.second) # Imprimimos los segundos.

# Vemos la clase date:
# La clase date es una subclase de la clase datetime.
# Esta clase se utiliza para representar una fecha, sin hora.

from datetime import date

current_time = date.today() # Inicializamos un objeto de tipo "date" con la fecha actual.

current_time = date(2023, 1, 1) # Inicializamos un objeto de tipo "date" con la fecha 1 de enero de 2023.

print(current_time) # Imprimimos la fecha 1 de enero de 2023.

print(current_time.year) # Imprimimos el año.
print(current_time.month) # Imprimimos el mes.
print(current_time.day) # Imprimimos el día.   


current_time = date(current_time.year, current_time.month + 1, current_time.day) # Inicializamos un objeto de tipo "date" y sumamos 1 al mes actual.

print(current_time) 

# Vemos la clase timedelta:
# La clase timedelta es una subclase de la clase datetime.
# Esta clase se utiliza para representar una duración, es decir, una diferencia entre dos fechas o dos horas.
# Esta clase se utiliza para realizar operaciones con fechas y horas.

diff= datetime.now() - year_2023 # Inicializamos un objeto de tipo "timedelta" con la diferencia entre la fecha actual y la fecha 1 de enero de 2023.
print(diff) # Imprimimos la diferencia entre la fecha actual y la fecha 1 de enero de 2023.
diff= year_2023.date() - current_time # Inicializamos un objeto de tipo "timedelta" con la diferencia entre la fecha 1 de enero de 2023 y la fecha actual.
print(diff) # Imprimimos la diferencia entre la fecha 1 de enero de 2023 y la fecha actual.