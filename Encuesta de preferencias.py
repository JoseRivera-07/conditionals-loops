print("Programa de encuesta: ¿Te gusta programar?\n")

si_count = 0
no_count = 0

while True:
    edad_input = input("Ingresa tu edad (0 o negativa para salir): ")

    # Validación de edad vacía o no numérica
    if edad_input.strip() == "" or not edad_input.isdigit():
        print("❌ Error: ingresa una edad válida.")
        continue

    edad = int(edad_input)

    # Si es cero o negativa, terminamos
    if edad <= 0:
        break

    # Preguntar si le gusta programar
    while True:
        respuesta = input("¿Te gusta programar? (sí/no): ").strip().lower()

        if respuesta == "":
            print("❌ No puedes dejar la respuesta vacía.")
        elif respuesta not in ("si", "sí", "no"):
            print("❌ Respuesta inválida. Debe ser 'sí' o 'no'.")
        else:
            # Contabilizar respuestas
            if respuesta in ("si", "sí"):
                si_count += 1
            else:
                no_count += 1
            break

# Al finalizar
print("\n--- RESULTADOS FINALES ---")
print(f"Respuestas afirmativas: {si_count}")
print(f"Respuestas negativas:   {no_count}")
