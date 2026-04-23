# =========================
# MANEJO DE EXCEPCIONES
# =========================

def divide_numbers():
    try:
        # Pedimos datos al usuario
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el denominador: "))

        # Operación que puede fallar
        result = a / b

    # -------------------------
    # TIPOS DE ERRORES
    # -------------------------

    except ZeroDivisionError:
        print("No se puede dividir entre cero ❌")

    except ValueError:
        print("Por favor, ingresa solo números válidos ❌")

    except Exception as error:
        # Captura cualquier otro error inesperado
        print(f"Error inesperado: {type(error).__name__}")

    # -------------------------
    # SE EJECUTA SI NO HAY ERROR
    # -------------------------
    else:
        print(f"Resultado: {result}")
        return result

    # -------------------------
    # SIEMPRE SE EJECUTA
    # -------------------------
    finally:
        print("Gracias por usar nuestra calculadora 👋")


# Ejecutar función
divide_numbers()
