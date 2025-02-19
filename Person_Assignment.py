class Person:
    def __init__(self, name, country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

P1 = Person("Yashada", "India", "02/03/2000")

print(P1.date_of_birth)
