# Diga si un número es par o impar
print("Introduce un numero para determinar si es par o impar")
numero= float(input("Numero: "))
absoluto = abs(numero)
print(numero)
div1 = absoluto/2
div2 = absoluto//2
if div1 == div2: 
    print("par")
else:
    print("impar")
