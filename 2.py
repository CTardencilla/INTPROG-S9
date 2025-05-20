numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

suma_total = sum(numeros)
print("Suma total:", suma_total)
