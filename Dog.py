class Dog:
    def __init__(self, color, breed, age):
        self.color = color
        self.breed = breed
        self.age = age

    def bark(self):
        return "Bhow Bhow"

D = Dog("Black", "Retriever", 5)
print(D.color, D.breed, D.age)
print(D.bark())