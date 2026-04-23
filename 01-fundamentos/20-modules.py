# =========================
# IMPORTACIÓN DE MÓDULOS
# =========================

# Importamos un módulo completo
import math_utils

# Importamos un módulo desde un paquete
from my_package import messages

# -------------------------
# USO DE FUNCIONES
# -------------------------

# Llamamos función del módulo
result = math_utils.addition(3, 4)
print(result)

# Llamamos funciones del paquete
print(messages.greet("Ricardo"))
print(messages.bye("Ricardo"))