# =========================
# CLASE ABSTRACTA + HERENCIA + POLIMORFISMO
# =========================

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance  # encapsulación (privado)

    # -------------------------
    # MÉTODO COMÚN
    # -------------------------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    # -------------------------
    # MÉTODOS INTERNOS (PROTEGIDOS)
    # -------------------------
    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance

    # -------------------------
    # MÉTODO ABSTRACTO
    # -------------------------
    @abstractmethod
    def withdraw(self, amount):
        pass  # cada clase hija lo implementa distinto

    # -------------------------
    # MÉTODO DE CONSULTA
    # -------------------------
    def check_balance(self):
        return f"Saldo actual: ${self.__balance}"


# =========================
# CLASE HIJA: CUENTA AHORRO
# =========================

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        penalty = amount * 0.05  # comisión 5%
        total = amount + penalty

        if total <= self._get_balance():
            self._set_balance(self._get_balance() - total)
            return f"Retiro exitoso (incluye comisión: {penalty})"
        return "Fondos insuficientes ❌"


# =========================
# CLASE HIJA: CUENTA NÓMINA
# =========================

class PayrollAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
            return "Retiro exitoso ✅"
        return "Fondos insuficientes ❌"


# =========================
# USO (POLIMORFISMO)
# =========================

accounts = [
    SavingAccount("Ricardo", 1000),
    PayrollAccount("Ricardo", 1000)
]

# Misma interfaz, diferente comportamiento
for account in accounts:
    print(account.withdraw(100))
    print(account.check_balance())