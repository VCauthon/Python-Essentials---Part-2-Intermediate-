def is_prime(num):
    #
    # Write your code here.
    #

    # Se crea la variable para indicar si el numero es primo
    es_primo = True

    # Se realiza un blucle FOR para iterar todos los valores
    for valor in range(1, num + 1):

        # Se revisa si el numero iterado es distinto a 1 o el propio numero recibido
        if valor != num and valor != 1:

            # Se comprueba si la iteración es divisible por el número recibido
            if num % valor == 0:
                # Se indica que este es un número primo
                es_primo = False

                # Se finaliza el bucle
                break

    # Se devuelven los resultados obtenidos
    return es_primo


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
