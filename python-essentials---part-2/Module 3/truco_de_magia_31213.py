"""
A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that the code:

will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
"""
# Número que debe descrubir en el while
secret_number = 777

# Número elegido por consola
numero_elegido = 0

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while secret_number != numero_elegido:

    # Se indica el mensaje de que sigue atrapado
    print("Ha ha! You're stuck in my loop!")

    # Se pregunta que número quiere elegir
    numero_elegido = int(input("Que número probaras? \n"))

# Se indica el mensaje de que ha logrado salir del bucle
print("Well done, muggle! You are free now.")

