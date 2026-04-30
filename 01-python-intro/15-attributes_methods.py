# =========================
# ATRIBUTOS Y MÉTODOS EN CLASES
# =========================

class Person:

    # -------------------------
    # ATRIBUTO DE CLASE
    # -------------------------
    species = "Humano"  # compartido por TODOS los objetos

    def __init__(self, name, age):
        # -------------------------
        # ATRIBUTOS DE INSTANCIA
        # -------------------------
        self.name = name        # público
        self.age = age          # público
        self._energy = 100      # protegido (convención)
        self.__password = "1234"  # privado (name mangling)

    # -------------------------
    # MÉTODO PÚBLICO
    # -------------------------
    def work(self):
        return f"{self.name} está trabajando duro."

    # -------------------------
    # MÉTODO PROTEGIDO
    # -------------------------
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy

    # -------------------------
    # MÉTODO PRIVADO
    # -------------------------
    def __generate_password(self):
        return f"$${self.name}{self.age}$$"


# =========================
# CREACIÓN DE OBJETOS
# =========================

person1 = Person("Ricardo", 29)
person2 = Person("Fernando", 16)

# =========================
# USO DE MÉTODOS
# =========================

print(person1.work())
print(person1._waste_energy(10))  # funciona, pero es "interno"

# print(person1.__generate_password()) ❌ ERROR (privado)

print(person2.work())