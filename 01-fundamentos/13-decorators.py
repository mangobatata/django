# =========================
# DECORADORES EN PYTHON
# =========================

# Un decorador es una función que envuelve otra función
# para agregar lógica extra (ej: autenticación)

def require_auth(func):
    # wrapper reemplaza temporalmente a la función original
    def wrapper(user):
        # .lower() → hace la comparación sin importar mayúsculas
        if user.lower() == "admin":
            return func(user)  # ejecuta la función original
        else:
            return "Acceso denegado 🚫"

    return wrapper


# -------------------------
# USO DEL DECORADOR
# -------------------------

@require_auth
def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"


# -------------------------
# PRUEBAS
# -------------------------

print(admin_dashboard("Admin"))   # permitido
print(admin_dashboard("ADMIN"))   # permitido (gracias a .lower())
print(admin_dashboard("user"))    # denegado