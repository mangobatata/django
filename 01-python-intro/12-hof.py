# =========================
# HIGHER-ORDER FUNCTIONS (HOF)
# =========================

# Una HOF es una función que:
# - recibe otra función como argumento
# - o retorna una función

# -------------------------
# DECORADOR (FUNCION QUE ENVUELVE OTRA)
# -------------------------

def require_auth(func):
    # wrapper es una función interna
    def wrapper(user):
        # Validación de usuario
        if user.lower() == "admin":
            return func(user)  # ejecuta la función original
        else:
            return "Acceso denegado 🚫"

    return wrapper  # retorna la función wrapper


# -------------------------
# FUNCIÓN ORIGINAL
# -------------------------

def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"


# -------------------------
# APLICANDO EL DECORADOR MANUALMENTE
# -------------------------

auth_view_dashboard = require_auth(admin_dashboard)

print(auth_view_dashboard("Admin"))     # permitido
print(auth_view_dashboard("Invitado"))  # denegado


# =========================
# FORMA PRO (DECORADOR CON @)
# =========================

@require_auth
def admin_panel(user):
    return f"Panel PRO para {user}"

print(admin_panel("admin"))
print(admin_panel("user"))