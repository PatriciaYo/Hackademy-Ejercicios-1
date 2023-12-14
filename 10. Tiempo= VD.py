#  Reciba la velocidad y la distancia que tiene que recorrer un carro y entrega cuánto tiempo le tomaría recorrer esa distancia.
import datetime as dt


velocidad = float(input("Escribir Velocidad en k/h: " ,))
	
distancia =	float(input("Escribir Distancia en k: ",))

tiempo =  distancia / velocidad	
horas = dt.timedelta(hours=tiempo)
print(tiempo)
print(horas)