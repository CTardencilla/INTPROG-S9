numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

numeros_invertidos = list(reversed(numeros))
print("Lista en orden inverso:", numeros_invertidos)
