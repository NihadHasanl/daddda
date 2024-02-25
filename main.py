class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.name} и мне {self.age} лет."


person1 = Person(name="Алиса", age=30)
print(person1.greet())
