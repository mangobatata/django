# =========================
# BUCLES (FOR LOOP) EN PYTHON
# =========================

# Un bucle permite repetir acciones varias veces

# -------------------------
# EJEMPLO 1: SUMAR ELEMENTOS
# -------------------------

my_list = [1, 2, 3, 4, 5]
addition = 0  # acumulador

for number in my_list:
    print(number)
    addition += number  # suma cada número

print("Suma total:", addition)

# -------------------------
# EJEMPLO 2: RANGE + ENUMERATE
# -------------------------

# range(100) → genera números del 0 al 99
# list(range(100)) → convierte eso en lista (no siempre necesario)

# enumerate() → devuelve:
# (índice, valor)

for index, number in enumerate(range(100)):
    print(index, number * 2)

# -------------------------
# EJEMPLO EXTRA (PERSONALIZAR INDEX)
# -------------------------

# Podés empezar el índice desde otro número
for index, number in enumerate(range(5), start=1):
    print(f"Posición {index} → Valor {number}")