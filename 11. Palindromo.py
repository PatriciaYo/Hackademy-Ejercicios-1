#– Valide si una palabra o frase es palindromo. – Reciba un año y te responda si es o no es bisiesto.
#frase = "1Probando Odnaborp 2"
frase = input("Introduce una frase: ",)
original = frase
#Quitar espacios
frase = frase.replace(" ", "")

#Minusculas
frase = frase.lower()

#Reversa
frase_rev = frase[::-1]

if frase == frase_rev:
    print(original, "ES PALINDROMO")
else:
    print(original, "NO ES PALINDROMO")