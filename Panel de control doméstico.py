# Estados iniciales
es_noche = True     # Puedes cambiarlo a False para probar
luces_encendidas = False
calefaccion_activada = False
temperatura = 16     # Cambia este valor para probar

def mostrar_estado():
    print("\n--- ESTADO DE LA VIVIENDA ---")
    print(f"¿Es de noche?: {'Sí' if es_noche else 'No'}")
    print(f"Luces encendidas: {'Sí' if luces_encendidas else 'No'}")
    print(f"Temperatura actual: {temperatura} °C")
    print(f"Calefacción activada: {'Sí' if calefaccion_activada else 'No'}\n")

while True:
    print("=== MENÚ DE CONTROL ===")
    print("1. Encender luces")
    print("2. Activar calefacción")
    print("3. Ver estado")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        if es_noche:
            if not luces_encendidas:
                luces_encendidas = True
                print("✔ Luces encendidas.")
            else:
                print("Las luces ya estaban encendidas.")
        else:
            print("❌ No puedes encender las luces durante el día.")

    elif opcion == "2":
        if temperatura < 18 and luces_encendidas:
            if not calefaccion_activada:
                calefaccion_activada = True
                print("✔ Calefacción activada.")
            else:
                print("La calefacción ya estaba activada.")
        else:
            print("❌ No es posible activar la calefacción.")
            if temperatura >= 18:
                print("→ La temperatura es demasiado alta.")
            if not luces_encendidas:
                print("→ Las luces deben estar encendidas.")

    elif opcion == "3":
        mostrar_estado()

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("❌ Opción inválida. Intenta nuevamente.")
