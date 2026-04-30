# =========================
# DATA TYPES EN PYTHON
# =========================

# Un DATA TYPE (tipo de dato) define qué tipo de valor guarda una variable
# Python detecta automáticamente el tipo según el valor asignado

# -------------------------
# STRING (str) → TEXTO
# -------------------------
name = "Ricardo"          # str: cadena de texto (usa comillas)
last_name = "Cuéllar"     # str

# -------------------------
# INTEGER (int) → ENTEROS
# -------------------------
number = 2000             # int: número sin decimales
age = 29                  # int
waste = 25                # int

# -------------------------
# FLOAT (float) → DECIMALES
# -------------------------
decimal = 20.42           # float: número con punto decimal
temp = 27.3               # float

# -------------------------
# BOOLEAN (bool) → TRUE / FALSE
# -------------------------
boolean = True            # bool: verdadero (equivale a 1)
boolean_false = False     # bool: falso (equivale a 0)
is_gamer = True           # bool

# =========================
# VERIFICAR EL TIPO DE DATO
# =========================

# type() nos dice qué tipo de dato es cada variable
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(temp))       # <class 'float'>
print(type(is_gamer))   # <class 'bool'>

# =========================
# USO DE VARIABLES SEGÚN SU TIPO
# =========================

# Strings → se pueden concatenar
print("Nombre:", name, last_name)

# Int / Float → se pueden operar matemáticamente
total = number + waste
print("Total:", total)

# Boolean → se usan para decisiones
if is_gamer:
    print("Le gustan los videojuegos 🎮")
else:
    print("No juega videojuegos")

# =========================
# FORMA MODERNA (f-strings)
# =========================

# Permite mezclar texto + variables fácilmente
print(f"{name} {last_name} tiene {age} años y la temperatura es {temp}°C")