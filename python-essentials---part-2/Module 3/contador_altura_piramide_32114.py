"""
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

The figure illustrates the rule used by the builders:



Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

Test your code using the data we've provided.


Test Data

Sample input: 6
Expected output: The height of the pyramid: 3

Sample input: 20
Expected output: The height of the pyramid: 5

Sample input: 1000
Expected output: The height of the pyramid: 44

Sample input: 2
Expected output: The height of the pyramid: 1
"""

# Se iteran los casos con los que se hara la prueba
for numero_bloques in [6, 20, 1000, 2]:

    # Se almacena el número de bloques
    #blocks = int(input("Enter the number of blocks: "))
    blocks = numero_bloques

    # Se crea la variable para calcular la altura
    height = 0

    # Se crea la variable para saber el tamaño de la última línea
    ultimo_tam_linea = 0

    # Se crea la variable para saber cuantos bloques hay en la línea actual
    bloques_linea_actual = 0

    #
    # Write your code here.
    #

    # Se itera el número de bloques que hay
    for bloque in range(blocks):

        # Se actualizan los bloques actuales
        numero_bloques -= 1
        bloques_linea_actual += 1

        # Se comprueba si la línea actual ya tiene un tamaño superior a la última línea
        if ultimo_tam_linea < bloques_linea_actual:

            # Se actualiza el tamaño máximo de la última línea
            ultimo_tam_linea = bloques_linea_actual

            # Se reinicia el número de bloques de la línea actual
            bloques_linea_actual = 0

            # Se incrementa el tamaño de la piramide
            height += 1


    print("The height of the pyramid:", height)
