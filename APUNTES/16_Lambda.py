## Lambda Funciones ##
# Las funciones lambda son funciones anónimas que se pueden definir en una sola línea. Se utilizan principalmente para funciones pequeñas y simples.

sum_two_values = lambda x, y: x + y # Definimos una función lambda que suma dos valores.
print(sum_two_values(5, 10)) # Imprimimos el resultado de la función lambda.

def suma(z):
    return lambda x, y: x + y -z # Definimos una función que devuelve una función lambda que suma dos valores y resta un tercer valor que pertenece a la función.

print(suma(5)(10, 20)) # Imprimimos el resultado de la función que devuelve una función lambda. Se deben ingresar dos valores para la función lambda y un valor para la función que devuelve la función lambda.