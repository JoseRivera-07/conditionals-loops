usuario_correcto = "admin"
clave_correcta = "1234"

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # 1. Si ambos campos están vacíos, NO cuenta como intento
    if usuario == "" and contraseña == "":
        print("Campos vacíos. Este intento no cuenta.")
        continue

    # Aumentar intentos solo si los campos no están vacíos
    intentos += 1

    # 2. Validar usuario y contraseña con operadores lógicos
    if usuario == usuario_correcto and contraseña == clave_correcta:
        print("\n Inicio de sesión exitoso. ¡Bienvenido!")
        break
    else:
        # Motivos de fallo
        if usuario != usuario_correcto and contraseña != clave_correcta:
            print(" Usuario y contraseña incorrectos.")
        elif usuario != usuario_correcto:
            print(" Usuario incorrecto.")
        else:
            print(" Contraseña incorrecta.")

        print(f"Intentos usados: {intentos}/{max_intentos}")

# Fin del bucle
if intentos == max_intentos:
    print("\n Has alcanzado el número máximo de intentos.")
