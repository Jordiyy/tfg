import pandas as pd
import csv
import math


datos = []
with open("score_manual.csv", mode='r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        datos.append(row)


columnas_necesarias = ['age', 'ldl', 'colt', 'systolic_blood_pressure', 'smoke']
for columna in columnas_necesarias:
    if columna not in datos[0]:
        raise KeyError(f"Columna necesaria '{columna}' no encontrada en el CSV")


for row in datos:
    age = float(row['age'])
    ldl = float(row['ldl'])
    colt = float(row['colt'])
    systolic_blood_pressure = float(row['systolic_blood_pressure'])
    smoke = float(row['smoke'])
    
    score = (age / 365 / 80) * ((ldl / colt) * ((systolic_blood_pressure / 50) - 0.5) * (1.5 * smoke))
    row['score'] = round(math.exp(score), 2)


with open('score_low_systolic.csv', mode='w', newline='') as file:
    fieldnames = datos[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(datos)

print("Cálculo completado y guardado en 'score_low_systolic.csv'")