class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age_calculate(self, current_date, birth_date):
        self.current_date = current_date
        self.birth_date = birth_date
        return self.current_date - self.birth_date

P1 = Person("Yashada", "India", "02/03/2000")
P1.age_calculate("21/02/2025", "02/03/2000")
print(P1.name, P1.country, P1.date_of_birth)
# print(P1.age_calculate())


