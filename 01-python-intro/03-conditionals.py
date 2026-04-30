# =========================
# CONDICIONALES EN PYTHON
# =========================

# Las variables booleanas (True / False) se usan para tomar decisiones
is_new_dev = False
interest_python = True
knows_python = False

# -------------------------
# ESTRUCTURA IF / ELIF / ELSE
# -------------------------

# if → evalúa la primera condición
# elif → evalúa otra condición si la anterior fue False
# else → se ejecuta si ninguna condición se cumple

if is_new_dev:
    print("Te recomiendo empezar con Python 🐍")

elif interest_python:
    print("Aprende en mi curso de Fundamentos de Python 🚀")

else:
    print("Inicia en el mundo de la programación 💻")

# -------------------------
# SEGUNDO BLOQUE CONDICIONAL
# -------------------------

# Este bloque es independiente del anterior

if knows_python:
    print("Te recomiendo aprender Django 🌐")
else:
    print("Primero fortalece tus bases en Python 📘")