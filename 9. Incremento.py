# Calcule el incremento salarial de una persona: Si su salario es menor a 15mil el incremento será del 20% y si es mayor a 15mil el incremento será del 15%

salario = float(input("Escribe tu salario en pesos sin simbolos ",))

if salario > 15000:
    incremento = salario * .15
    print("Tu incremento será del 15%, equivalente a",incremento )
else:
    incremento = salario * .20
    print("Tu incremento será del 20%, equivalente a",incremento )
