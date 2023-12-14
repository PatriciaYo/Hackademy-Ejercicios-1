# – Reciba un año y te responda si es o no es bisiesto.
# Definición https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto
ano = int(input("Escribe un año: ",))

if ano//4 != ano/4:
		resultado = "No es bisiesto"
# elif ano-((ano//100)*100)==0 and ano//400 !=  ano/400:
elif ano%100 == 0 and ano//400 !=  ano/400:
        resultado = "No es bisiesto"
else:
    resultado = "Es bisiesto"
print(resultado)