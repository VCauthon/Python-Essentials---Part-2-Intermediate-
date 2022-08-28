"""
The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.

It can be used with both the while and for loops.

Your task here is very special: you must design a vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
"""

# Palabras con las que se hace la prueba
palabras = ["Gregory","abstemious","IOUEA"]
for user_word in palabras:

    # Se saca por pantalla la palabra deletreada sin volcales
    print("\n", user_word.upper())

    # Se crea la variable para acumular las letras que no se han eliminado
    palabra_sin_vocales = ""

    # Prompt the user to enter a word
    # and assign it to the user_word variable.

    for letter in user_word:

        # Complete the body of the for loop.
        if letter.upper() in ["A", "E", "I", "O", "U"]:

            # Se vuelve al for
            continue

        # Se saca por pantalla la letra
        print(letter.upper())
        palabra_sin_vocales += letter.upper()

    # Se saca por pantalla la palabra
    print(palabra_sin_vocales)