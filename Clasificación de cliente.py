monto = input("Ingrese el valor total de la compra: ")

# Validación del monto
if not monto.isdigit():
    print("❌ Error: el monto ingresado no es válido.")
else:
    monto = float(monto)
    if monto < 0:
        print("❌ Error: el monto no puede ser negativo.")
    else:
        membresia = input("Tipo de membresía (activa, temporal o ninguna): ").lower()

        print("\n--- CLASIFICACIÓN ---")

        # Clasificaciones según condiciones
        if monto >= 500000 and membresia == "activa":
            print("✔ Cliente Premium")

        elif (200000 <= monto < 500000) or membresia == "temporal":
            print("✔ Cliente Frecuente")

        else:
            print("✔ Cliente Regular")
