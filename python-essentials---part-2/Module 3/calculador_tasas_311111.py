#income = float(input("Enter the annual income: "))
income = float(-100)

#
# Write your code here.
#

# Variable para indicar el maximo permitido
maximo_permitido = 85528

# Se genera la variable con la que se presentara la tasa
tax = 0

# Revisa si la tasa no se ha superado
if income < maximo_permitido:

    # Se aplica la tasa sobre la entrada anual
    tax = income * 0.18

    # Se incluye la base inponible
    tax = tax - 556.2


# Revisa si la tasa se ha superado
elif income > maximo_permitido:

    # Se calcula cual el sueldo sobre el que se calculara el 32%
    tax = (income - maximo_permitido) * 0.32

    # Se incluye la base a pagar
    tax = tax + 14839.2

# Se revisa si el calculo de tasas sale a devolver
if tax < 0: tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
