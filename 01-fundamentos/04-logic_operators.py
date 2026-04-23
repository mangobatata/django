# =========================
# OPERADORES LÓGICOS EN PYTHON
# =========================

# Se usan para combinar o modificar condiciones (True / False)

# -------------------------
# AND → ambas condiciones deben ser True
# -------------------------
age = 18
licensed = False

# True AND False → False
if age >= 18 and licensed:
    print("Puedes manejar")
else:
    print("No puedes manejar 🚫")

# -------------------------
# OR → al menos una condición debe ser True
# -------------------------
is_student = False
membership = False

# False OR False → False
if is_student or membership:
    print("Obtiene precio especial 💸")
else:
    print("No aplica descuento")

# -------------------------
# NOT → invierte el valor
# -------------------------
is_admin = True

# NOT True → False
if not is_admin:
    print("Acceso denegado 🚫")
else:
    print("Acceso permitido ✅")

# -------------------------
# SHORT CIRCUITING
# -------------------------

# Python evalúa de izquierda a derecha y se detiene cuando ya conoce el resultado

name = "Ricardo"

# En "and":
# Si el primer valor es falso → devuelve ese valor
# Si es verdadero → devuelve el segundo

print(name and name.upper())  # "RICARDO"

# Ejemplo extra:
print("" and "Hola")   # "" → se detiene (string vacío es False)
print("Hola" and 123)  # 123 → ambos True, devuelve el último

# En "or":
# Devuelve el primer valor verdadero que encuentre

print("" or "Default")   # "Default"
print("Hola" or "Otro")  # "Hola"