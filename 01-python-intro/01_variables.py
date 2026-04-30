# Una VARIABLE es un espacio en memoria donde guardamos un dato
# Tiene un nombre (identificador) y un valor

# Variable tipo texto (string)
name = "Ricardo"  # guarda el nombre

# Otra variable de texto
full_name = "Ricardo Cuéllar"  # nombre completo

# Convención: variables con "_" al inicio suelen considerarse "privadas"
_private_name = "Richie"

# Variable numérica (float)
PI = 3.1416  # constante matemática aproximada

# Convención: MAYÚSCULAS se usan para constantes (valores que no cambian)
GREET = "Hola"

# Imprimir variables en pantalla
print(name)
print(full_name)

# Ejemplo combinando variables
print(GREET + ", " + name)

# Forma moderna con f-strings (recomendado)
print(f"{GREET}, {full_name}")
