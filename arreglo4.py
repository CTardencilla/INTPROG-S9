import os
import random

part=list()
while True:
    nombre= input("Ingrese el nombre del participante (o 'fin' para terminar ): ")

    if nombre.lower() == 'fin':
        break
    part.append(nombre.upper())

os.system("cls/clear")
print('participantes registrados')
print(part)