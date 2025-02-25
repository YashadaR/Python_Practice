class Emplyoee:
    company_name = "XYZ" 
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

E = Emplyoee("ABC", 40000, "Developer")
print(E.name, E.salary, E.designation)