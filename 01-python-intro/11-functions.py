# =========================
# FUNCIONES EN PYTHON
# =========================

# Una función es un bloque de código reutilizable

# -------------------------
# PARÁMETROS Y ARGUMENTOS
# -------------------------

# Parámetros → variables que recibe la función
def hello(greet="Hola", name="Invitado"):
    print(f"{greet}, {name}")

# Argumentos → valores que enviamos a la función
hello("Hola", "Ricardo")
hello("Ciao", "Fernando")

# Usando valores por defecto
hello()

# Argumentos por nombre (keyword arguments)
hello(name="Teddy", greet="Hello")


# -------------------------
# *args → argumentos ilimitados (tupla)
# -------------------------

# *args permite recibir muchos valores sin definirlos uno por uno
def sum_numbers(*args):
    print(args)  # es una TUPLA
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # 10


# -------------------------
# **kwargs → argumentos con clave=valor (diccionario)
# -------------------------

# **kwargs permite recibir datos tipo clave:valor
def show_user(**kwargs):
    print(kwargs)  # es un DICCIONARIO

show_user(name="Ricardo", age=29)


# -------------------------
# *args + **kwargs juntos
# -------------------------

def big_function(*args, **kwargs):
    print("args (tupla):", args)
    print("kwargs (diccionario):", kwargs)
    return kwargs

result = big_function(
    1, 2, 3, 4, 5, 6, 7,
    num1=77,
    num2=100
)

print("Retorno:", result)