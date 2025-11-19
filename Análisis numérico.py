print("Ingrese tres números enteros:")
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

# Contadores
positivos = 0
negativos = 0
ceros = 0

# Clasificación individual
for n in (a, b, c):
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        ceros += 1

# Análisis de combinaciones
print("\n--- RESULTADOS ---")

# 1. ¿Los tres son positivos?
if positivos == 3:
    print("✔ Los tres números son positivos.")

# 2. ¿Al menos uno es negativo?
elif negativos >= 1:
    print("✔ Al menos uno es negativo.")

# 3. ¿Exactamente uno es cero?
elif ceros == 1:
    print("✔ Exactamente uno de los números es cero.")

# 4. Si no cae en ninguno, mostramos combinaciones restantes
else:
    print("Ninguna condición principal se cumplió.")
