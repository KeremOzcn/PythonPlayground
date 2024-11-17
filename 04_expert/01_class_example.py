class Person:
    # Defines a class named Person.
    def __init__(self, name, age):
        # Initializes the object with name and age.
        self.name = name
        self.age = age

    def introduce(self):
        # Defines a method to introduce the person.
        return f"My name is {self.name} and I am {self.age} years old."

# Create multiple Person instances
person1 = Person("Kerem", 21)
person2 = Person("Eda", 18)
person3 = Person("Ahmet", 30)

# Store them in a list for easier management
people = [person1, person2, person3]

# Introduce each person
for person in people:
    print(person.introduce())