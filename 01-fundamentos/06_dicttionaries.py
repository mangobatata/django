# =========================
# DICCIONARIOS EN PYTHON
# =========================

# Un diccionario (dict) es una colección de datos en formato:
# clave (key) : valor (value)

user = {
    "name": "Ricardo",                # clave: string → valor: string
    "age": 29,                       # clave: string → valor: int
    "email": "ricardo@email.com",    # string → string
    "active": True,                  # string → boolean
    (19.12, -98.32): "Cancún México" # clave tipo tupla → valor string
}

# =========================
# MODIFICAR VALORES
# =========================

# Cambiar valores existentes
user["name"] = "Richard"
user["age"] = 27

# Agregar nueva clave
user["country"] = "México"

# =========================
# ACCEDER A VALORES
# =========================

# Acceder por clave
print(user["name"])  # Richard

# Acceder a clave tipo tupla
print(user[(19.12, -98.32)])

# =========================
# MÉTODOS IMPORTANTES
# =========================

# keys() → devuelve todas las claves
print(user.keys())

# values() → devuelve todos los valores
print(user.values())

# items() → devuelve pares (clave, valor)
print(user.items())

# =========================
# RECORRER UN DICCIONARIO
# =========================

for key, value in user.items():
    print(f"{key} → {value}")

# =========================
# VERIFICAR SI EXISTE UNA CLAVE
# =========================

if "email" in user:
    print("El usuario tiene email")

# =========================
# ELIMINAR ELEMENTOS
# =========================

# Elimina una clave
del user["active"]

# =========================
# RESULTADO FINAL
# =========================

print(user)