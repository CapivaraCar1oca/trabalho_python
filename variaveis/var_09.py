dias = int(input("Quantos dias? "))
horas = int(input("Quantas horas? "))
minutos = int(input("Quantos minutos? "))
segundos = int(input("Quantos segundos? "))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"O total de segundos é {total_segundos}.")
