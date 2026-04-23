# =========================
# WHILE LOOP EN PYTHON
# =========================

# Un while se ejecuta MIENTRAS una condición sea verdadera

# -------------------------
# EJEMPLO 1: CONTADOR
# -------------------------

counter = 1

while counter <= 5:
    print(f"Número: {counter}")
    counter += 1  # importante: evita bucle infinito
else:
    # El else se ejecuta cuando el while termina normalmente
    print("Terminamos contador ✅")

# -------------------------
# EJEMPLO 2: INPUT DEL USUARIO
# -------------------------

response = ''

# .lower() → convierte a minúsculas para evitar errores ("BYE", "Bye", etc.)
while response.lower() != 'bye':
    response = input("Escribe 'bye' para salir: ")
else:
    print("Terminamos programa 👋")