import random

numeros = [random.randint(1, 100) for _ in range(10)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Números generados:", numeros)
print("Pares:", pares)
print("Impares:", impares)
