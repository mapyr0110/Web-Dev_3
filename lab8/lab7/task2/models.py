
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return "Some generic animal sound"

    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}"

    def __str__(self):
        return f"Animal(Name: {self.name}, Age: {self.age}, Species: {self.species})"



class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def speak(self):  # Overriding
        return "auuuuuuuuf"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

    def __str__(self):
        return f"Dog(Name: {self.name}, Age: {self.age}, Breed: {self.breed})"



class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    def speak(self):  # Overriding 
        return "gaf gaf"

    def scratch(self):
        return f"{self.name} is scratching the furniture!"

    def __str__(self):
        return f"Cat(Name: {self.name}, Age: {self.age}, Color: {self.color})"