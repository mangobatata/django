# =========================
# TUPLAS EN PYTHON
# =========================

# Una TUPLA (tuple) es una colección ordenada de elementos
# Puede tener diferentes tipos de datos
# PERO es INMUTABLE → no se puede modificar

my_tuple = (1, 2, 3, 4, "Hola", True, False, 2, "hi", 3, 2)

# Imprimir la tupla completa
print(my_tuple)

# -------------------------
# ACCEDER A ELEMENTOS
# -------------------------

# Se accede por índice (empieza en 0)
print(my_tuple[1])  # 2

# -------------------------
# ERROR IMPORTANTE
# -------------------------

# Esto NO se puede hacer ❌
# porque las tuplas son inmutables

# my_tuple[1] = 20   # ❌ TypeError

# -------------------------
# CÓMO "MODIFICAR" UNA TUPLA
# -------------------------

# Convertir a lista → modificar → volver a tupla

temp_list = list(my_tuple)
temp_list[1] = 20

my_tuple = tuple(temp_list)
print(my_tuple)

# -------------------------
# OTRA TUPLA (EJEMPLO)
# -------------------------

week = ('Lunes', 'Martes', 'Miércoles')

print(week)

# -------------------------
# RECORRER UNA TUPLA
# -------------------------

for day in week:
    print(day)