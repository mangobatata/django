# =========================
# SETS EN PYTHON
# =========================

# Un SET (conjunto) es una colección:
# - NO ordenada
# - SIN elementos duplicados
# - Mutable (se puede modificar)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 2, 2, 2, 3, 4, 9, 10, 2, 5, 6}

# Los valores repetidos se eliminan automáticamente
print(my_set)

# -------------------------
# EJEMPLO CON STRINGS
# -------------------------

usernames = {"ricardo", "fernando", "devi", "fernando", "fernando1"}

# "fernando" repetido se elimina
print(usernames)

# -------------------------
# AGREGAR ELEMENTOS
# -------------------------

usernames.add("maria")
print(usernames)

# -------------------------
# ELIMINAR ELEMENTOS
# -------------------------

usernames.remove("devi")   # error si no existe
# usernames.discard("juan")  # no da error si no existe

print(usernames)

# -------------------------
# OPERACIONES DE CONJUNTOS
# -------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Unión (combina todo)
print(set1 | set2)   # {1,2,3,4,5}

# Intersección (comunes)
print(set1 & set2)   # {3}

# Diferencia
print(set1 - set2)   # {1,2}

# -------------------------
# VERIFICAR EXISTENCIA
# -------------------------

if "ricardo" in usernames:
    print("Usuario encontrado ✅")