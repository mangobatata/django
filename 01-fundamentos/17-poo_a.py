# =========================
# CLASE: CUENTA BANCARIA
# =========================

class BankAccount:
    def __init__(self, owner, initial_balance):
        # Atributos públicos
        self.owner = owner

        # Atributo privado (encapsulación)
        self.__balance = initial_balance

    # -------------------------
    # MÉTODO: DEPOSITAR
    # -------------------------
    def deposit(self, amount):
        # Validación básica
        if amount > 0:
            self.__balance += amount
        else:
            print("Monto inválido ❌")

    # -------------------------
    # MÉTODO: RETIRAR
    # -------------------------
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Saldo insuficiente o monto inválido ❌")

    # -------------------------
    # MÉTODO: CONSULTAR SALDO
    # -------------------------
    def check_balance(self):
        return f"Saldo actual: ${self.__balance}"

    # -------------------------
    # MÉTODO PRO (getter)
    # -------------------------
    def get_balance(self):
        return self.__balance


# =========================
# USO (ABSTRACCIÓN)
# =========================

# El usuario no necesita saber cómo funciona internamente
account = BankAccount("Ricardo", 1000)

account.deposit(500)
account.withdraw(200)

print(account.check_balance())
