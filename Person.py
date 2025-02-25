class Person:
    def __init__(self, first_name, Last_name):
        # self.height = height
        # self.age = age
        # self.native_State = native_State
        self.first_name = first_name
        self.last_name = Last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

P = Person("Yashada", "Raut")
# P1 = Person(5.1, 25, "Maharashtra")
# P2 = Person(5.5, 20, "Karnataka")   
# P3 = Person(6.1, 25, "Rajasthan")

# print(P1.height)
# print(P2.native_State)
# print(P3.age)
print(P.full_name())
