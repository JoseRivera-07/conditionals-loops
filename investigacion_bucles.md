# Investigación sobre Bucles en Programación

## 1. Diferencias entre un bucle controlado por contador y un bucle controlado por condición

### **Bucle controlado por contador**
- Se ejecuta un número **determinado y conocido** de veces.
- Usa una variable que actúa como contador.
- Ejemplo típico: `for`.

**Ejemplo:**
```python
for i in range(5):
    print("Hola")  # Se ejecuta exactamente 5 veces
```

### **Bucle controlado por condición**
- Se ejecuta **mientras se cumpla** una condición lógica.
- No siempre se sabe cuántas veces correrá.
- Ejemplo típico: `while`.

**Ejemplo:**
```python
numero = 5
while numero > 0:
    numero -= 1
```

---

## 2. Ejemplos cotidianos para cada tipo de bucle

### **Bucle controlado por contador (for)**
- Contar 10 repeticiones en el gimnasio.
- Hacer 20 llamadas telefónicas a una lista de clientes.
- Enviar 5 paquetes programados.

### **Bucle controlado por condición (while)**
- Continuar jugando un videojuego **mientras** tengas vidas.
- Regar una planta **mientras** el tanque tenga agua.
- Despertar **mientras** la alarma siga sonando.

---

## 3. ¿Cuándo es más apropiado usar `while` en lugar de `for`?

Usa **while** cuando:
- No conoces cuántas repeticiones habrá.
- Dependemos de una condición que puede cambiar en cualquier momento.
- El ciclo debe terminar al cumplirse un evento.

**Ejemplos ideales:**
- Validar datos de usuario.
- Leer datos hasta que el usuario escriba "salir".
- Programas que esperan un sensor o señal externa.

---

## 4. ¿Qué es un bucle infinito, cómo prevenirlo y cómo detectarlo?

### **Bucle infinito**
Es un ciclo que **nunca termina** porque la condición siempre es verdadera.

**Ejemplo:**
```python
while True:
    print("Esto nunca termina")
```

### **Cómo prevenirlo**
- Asegurar que la condición cambie dentro del ciclo.
- Modificar variables utilizadas en la condición.
- Usar sentencias como `break` cuando sea necesario.

### **Cómo detectarlo en ejecución**
- El programa no avanza.
- La CPU sube mucho.
- No hay salida a consola después de un punto esperado.
- La terminal parece "congelada".

---

## 5. Función de las sentencias `break` y `continue` dentro de un ciclo

### **break**
Termina el ciclo inmediatamente, sin importar si quedan más iteraciones.

**Ejemplo:**
```python
for i in range(10):
    if i == 5:
        break
```

### **continue**
Salta a la siguiente iteración sin ejecutar el resto del código del ciclo.

**Ejemplo:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 6. Error lógico más común al usar `while` y cómo evitarlo

### **Error común:**
Olvidar modificar la variable usada en la condición.

**Ejemplo incorrecto:**
```python
contador = 3
while contador > 0:
    print("Hola")  # Nunca cambia contador
```
Esto genera un bucle infinito.

### **Cómo evitarlo:**
- Asegurarse de actualizar las variables dentro del ciclo.
- Usar `print` de prueba para verificar el comportamiento.
- Revisar que la condición eventualmente pueda volverse falsa.

**Ejemplo correcto:**
```python
contador = 3
while contador > 0:
    print("Hola")
    contador -= 1
```

---

Fin del documento.