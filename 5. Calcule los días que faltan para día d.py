# Calcule los días que faltan para día de muertos y navidad
import datetime as dt

current= dt.date.today()
print(current)
navidad = dt.date(2023,12,24)
falta_nav = navidad - current
tipo= type(falta_nav)
days_navidad = falta_nav.days
print(days_navidad)
print("De hoy", current, "a navidad faltan", days_navidad, "dias." )

muertos = dt.date(2023,11,1)
falta_muertos = muertos - current
days_muertos = falta_muertos.days
print(days_muertos)
print("De hoy", current, "al día de muertos 2023 faltan", days_muertos, "dias." )

muertos2 = dt.date(2024,11,1)
falta_muertos2 = muertos2 - current
days_muertos2 = falta_muertos2.days
print(days_muertos2)
print("De hoy", current, "al día de muertos 2024 faltan", days_muertos2, "dias." )