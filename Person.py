class Person:
    def __init__(self, height, age, native_State):
        self.height = height
        self.age = age
        self.native_State = native_State

P1 = Person(5.1, 25, "Maharashtra")
P2 = Person(5.5, 20, "Karnataka")   
P3 = Person(6.1, 25, "Rajasthan")

print(P1.height)
print(P2.native_State)
print(P3.age)