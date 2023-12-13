# – Calcule el número de días que alguien ha vivido tomando en cuenta su fecha de nacimiento


import datetime as dt

current= dt.date.today()

nacimiento = input("Escribe tu fecha de nacimiento (formato YYYY-MM-DD): ")


nacimiento = dt.datetime.strptime(nacimiento, "%Y-%m-%d")
nacimiento = nacimiento.date()
resta = current-nacimiento
resta = resta.days
print(resta)