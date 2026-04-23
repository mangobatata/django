# =========================
# CLASES Y OBJETOS EN PYTHON
# =========================

# Una CLASE es como un "molde" para crear objetos
class Person:

    # Constructor → se ejecuta al crear el objeto
    def __init__(self, name, age):
        self.name = name  # atributo (propiedad)
        self.age = age

    # Método → función dentro de la clase
    def work(self):
        return f"{self.name} está trabajando duro."

    # Método extra (mejora)
    def introduce(self):
        return f"Hola, soy {self.name} y tengo {self.age} años."


# =========================
# CREACIÓN DE OBJETOS
# =========================

person1 = Person("Ricardo", 29)
person2 = Person("Fernando", 16)

# =========================
# USO DE MÉTODOS
# =========================

print(person1.work())
print(person2.work())

print(person1.introduce())
print(person2.introduce())