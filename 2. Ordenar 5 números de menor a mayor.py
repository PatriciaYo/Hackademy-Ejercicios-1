#2. Ordene 5 números de menor a mayor
print("Introduce 5 numeros")
n1= float(input("Ingresa primer numero: "))
n2= float(input("Ingresa segundo numero: "))
n3= float(input("Ingresa tercer numero: "))
n4= float(input("Ingresa cuarto numero: "))
n5= float(input("Ingresa quinto numero: "))
numeros = [n1,n2,n3,n4,n5]
numeros_ordenados = sorted(numeros)
print("Lista desordenada: ",numeros)
print("Linsta ordenada: ",numeros_ordenados)
