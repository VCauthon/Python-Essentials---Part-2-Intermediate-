"""
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

Test your code using the data we've provided.

Test Data

Sample input: 2000
Expected output: Leap year

Sample input: 2015
Expected output: Common year

Sample input: 1999
Expected output: Common year

Sample input: 1996
Expected output: Leap year

Sample input: 1580
Expected output: Not within the Gregorian calendar period

"""

entrada_years = [2000, 2015, 1999, 1996, 1580]

for valor in entrada_years:

    #year = int(input("Enter a year: "))
    # Variable donde se acumula el año
    year = valor
    year_type = ""

    #
    # Write your code here.
    #

    # Se comprueba si el year entra en el calendario gregorian
    if year < 1582:

        # Se indica el tipo de year
        year_type = "El año {} no forma parte del calendario gregorian".format(year)

    # Se comprueba si el year es divisible por 4
    elif (year % 4) != 0:

        # Se indica el tipo de year
        year_type = "El año {} es Common year (0)".format(year)

    # Se comprueba si el year es divisible por 100
    elif (year % 100) != 0:

        # Se indica el tipo de year
        year_type = "El año {} es leap year (1)".format(year)

    # Se comprueba si el year es divisible por 400
    elif (year % 400) != 0:

        # Se indica el tipo de year
        year_type = "El año {} es Common year (2)".format(year)

    # Se comprueba si no se ha cumplido ninguna de las condiciones
    else:

        # Se indica el tipo de year
        year_type = "El año {} es leap year (3)".format(year)

    # Se saca por pantalla que tipo de año es este
    print(year_type)