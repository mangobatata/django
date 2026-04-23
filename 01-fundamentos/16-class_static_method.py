# =========================
# CLASSMETHOD Y STATICMETHOD
# =========================

class Person:
    # Atributo de clase (compartido)
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # -------------------------
    # CLASS METHOD
    # -------------------------
    @classmethod
    def change_species(cls, new_species):
        # cls → referencia a la clase (NO al objeto)
        cls.species = new_species

    # -------------------------
    # STATIC METHOD
    # -------------------------
    @staticmethod
    def is_older(age):
        # No usa self ni cls
        return age >= 18


# =========================
# CREACIÓN DE OBJETOS
# =========================

person1 = Person("Ricardo", 29)
person2 = Person("Fernando", 35)

# -------------------------
# ATRIBUTO DE CLASE
# -------------------------

print(person1.species)
print(person2.species)

# Cambiamos el atributo de clase
Person.change_species("Reptiliano")

print(person1.species)
print(person2.species)

# -------------------------
# STATIC METHOD
# -------------------------

print(Person.is_older(20))                 # usando la clase
print(person1.is_older(person1.age))       # usando el objeto