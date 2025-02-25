class Car:
    car_count = 0

    def __init__(self, name, model):
        self.name = name
        self.model= model

        Car.car_count += 1

    @classmethod
    def new_car_count(cls):
        return f"Car count is {cls.car_count}"
    
C1 = Car("Honda", "City")
C2 = Car("Suzuki", "Baleno")

print(Car.new_car_count())
        